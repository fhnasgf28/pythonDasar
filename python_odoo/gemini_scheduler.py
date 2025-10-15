# -*- coding: utf-8 -*-
import logging
import google.generativeai as genai
import traceback
import sys
import os
import json
import requests
import random
import re
from odoo import api, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class GeminiMotivator(models.AbstractModel):
    """
    Model abstract untuk menampung logika cron job
    yang berinteraksi dengan Gemini AI dan Telegram.
    """
    _name = 'gemini.motivator'
    _description = 'Gemini Motivational Cron Job Logic'

    def _send_telegram_message(self, message):
        """
        Mengirim pesan ke Telegram
        """
        config_params = self.env['ir.config_parameter'].sudo()
        bot_token = config_params.get_param('gemini.telegram_bot_token')
        chat_id = config_params.get_param('gemini.telegram_chat_id')

        if not bot_token or not chat_id:
            _logger.warning("Telegram bot token or chat ID not configured. Message not sent.")
            return False

        try:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            data = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data, timeout=10)
            response.raise_for_status()
            return True
        except Exception as e:
            _logger.error(f"Failed to send Telegram message: {str(e)}")
            return False

    def _get_next_prompt(self, prompts):
        if not prompts:
            return None

        config_params = self.env['ir.config_parameter'].sudo()
        mode = (config_params.get_param('gemini.prompt_mode') or 'random').lower()

        if mode == 'sequential':
            try:
                raw_index = config_params.get_param('gemini.prompt_index') or '0'
                index = int(raw_index) % len(prompts)
            except Exception:
                index = 0
            # simpan indeks selanjutnya
            next_index = (index + 1) % len(prompts)
            try:
                config_params.set_param('gemini.prompt_index', str(next_index))
            except Exception:
                _logger.warning("Failed to persist gemini.prompt_index")
            return prompts[index].strip()
        # default: random
        return random.choice(prompts).strip()

    @api.model
    def _run_gemini_reminder_cron(self):
        """
        Metode ini dipanggil oleh cron job.
        Fungsinya: mengambil API key, memanggil Gemini, lalu mengirim notifikasi ke Telegram.
        """
        _logger.info("Starting Gemini Motivational Cron Job...")

        # 1. Ambil API Key dari System Parameters
        config_params = self.env['ir.config_parameter'].sudo()
        api_key = config_params.get_param('gemini.api_key')

        # DEBUG: print presence & masked key to help diagnosis
        try:
            print("DEBUG: gemini.api_key found?", bool(api_key))
            if api_key:
                masked = api_key[:4] + "..." + api_key[-4:] if len(api_key) > 8 else "****"
                print(f"DEBUG: gemini.api_key (masked): {masked}")
            sys.stdout.flush()
        except Exception:
            # jangan ganggu flow jika printing gagal
            _logger.exception("Failed to print debug api_key info")

        if not api_key:
            error_msg = "Gemini API Key tidak ditemukan di System Parameters (key: gemini.api_key). Cron job dibatalkan."
            _logger.warning(error_msg)
            self._send_telegram_message(f"❌ <b>Error:</b> {error_msg}")
            return

        # 2. Konfigurasi dan Panggil Gemini AI
        try:
            print("DEBUG: configuring genai with provided API key...")
            sys.stdout.flush()
            genai.configure(api_key=api_key)
            prompts = self._load_prompts_from_json()
            if not prompts:
                prompt = """
                Berikan satu wawasan atau saran yang realistis tentang salah satu topik berikut:
                - Strategi membangun kekayaan jangka panjang
                - Pengembangan karir dan peningkatan keterampilan profesional
                - Membangun kepercayaan diri yang tahan banting
                - Psikologi sukses dan pola pikir berkembang
                
                Sertakan contoh konkret yang bisa langsung diterapkan.
                Sampaikan dalam bahasa Indonesia yang jelas dan menginspirasi, maksimal 3 - 6 kalimat.
                """
            else:
                # pilih prompt sesuai mode (random atau sequential)
                prompt = self._get_next_prompt(prompts)
                if not prompt:
                    prompt = random.choice(prompts).strip()

            # coba model utama dulu (pakai model flash untuk akun free)
            tried_models = []
            success = False
            motivation_text = ""

            try:
                model_name = 'gemini-2.5-flash'
                tried_models.append(model_name)
                print(f"DEBUG: trying model {model_name}")
                sys.stdout.flush()
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                # ambil teks dari response dengan fallback
                try:
                    motivation_text = response.text.strip()
                except Exception:
                    motivation_text = str(response).strip()
                success = True
            except Exception as e_main:
                print("WARNING: primary model attempt failed:", e_main)
                traceback.print_exc()
                sys.stdout.flush()

            if not success or not motivation_text:
                error_msg = "Gagal mendapatkan respons dari model Gemini. Silakan coba lagi nanti."
                _logger.error(error_msg)
                self._send_telegram_message(f"❌ <b>Error:</b> {error_msg}")
                return

            # 3. Kirim pesan motivasi ke Telegram
            telegram_sent = self._send_telegram_message(f"💡 <b>Insight Hari Ini</b>\n\n{motivation_text}")

            if telegram_sent:
                _logger.info("Insight message sent to Telegram successfully")
            else:
                _logger.warning("Failed to send motivational message to Telegram")

        except Exception as e:
            error_msg = f"Terjadi kesalahan saat memproses permintaan Gemini: {str(e)}"
            _logger.error(error_msg)
            self._send_telegram_message(f"❌ <b>Error:</b> {error_msg}")
            traceback.print_exc()
    
    def _load_prompts_from_json(self):
        try:
            module_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            prompts_file = os.path.join(module_root, 'data', 'gemini_prompts.json')
            if not os.path.isfile(prompts_file):
                _logger.warning(f"Prompts file not found: {prompts_file}")
                return []
            with open(prompts_file, 'r', encoding='utf-8') as f:
                raw = f.read()
            # Coba parse normal dulu
            try:
                prompts = json.loads(raw)
            except Exception as e:
                _logger.info("Failed to parse prompts JSON normally, attempting to strip JS-style comments: %s", str(e))
                # Hapus komentar // dan /* */
                clean = re.sub(r'//.*?$|/\*.*?\*/', '', raw, flags=re.S | re.M)
                try:
                    prompts = json.loads(clean)
                except Exception as e2:
                    _logger.error("Failed to parse prompts JSON after stripping comments: %s", str(e2))
                    return []
            if not isinstance(prompts, list):
                _logger.warning("Prompts JSON is not a list: %s", type(prompts))
                return []
            
            cleaned = [str(p).strip() for p in prompts if isinstance(p, str) and p.strip()]
            if not cleaned:
                _logger.warning("Prompts list is empty after cleaning: %s", prompts_file)
            return cleaned
        except Exception as e:
            _logger.error(f"Failed to load prompts from JSON: {str(e)}")
            return []

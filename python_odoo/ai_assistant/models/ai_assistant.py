import logging
import requests
import json
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class AIAssistant(models.Model):
    _name = 'ai.assistant'
    _description = 'AI Assistant'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    active = fields.Boolean('Active', default=True)
    model = fields.Selection([
        ('gpt-3.5-turbo', 'GPT-3.5 Turbo'),
        ('gpt-4', 'GPT-4'),
        ('text-davinci-003', 'Text Davinci 003'),
    ], string='AI Model', default='gpt-3.5-turbo', required=True)
    temperature = fields.Float('Temperature', default=0.7, help="Controls randomness. Lower values make output more deterministic.")
    max_tokens = fields.Integer('Max Tokens', default=150, help="Maximum number of tokens to generate.")
    
    def _get_openai_api_key(self):
        """Get OpenAI API key from system parameters"""
        return self.env['ir.config_parameter'].sudo().get_param('openai.api_key')

    def generate_text(self, prompt):
        """Generate text using OpenAI's API"""
        api_key = self._get_openai_api_key()
        if not api_key:
            raise UserError(_("OpenAI API key is not configured. Please set it in Settings > General Settings."))

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        data = {
            'model': self.model,
            'messages': [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            'temperature': self.temperature,
            'max_tokens': self.max_tokens
        }

        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                data=json.dumps(data)
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content'].strip()
        except requests.exceptions.RequestException as e:
            _logger.error(f"OpenAI API Error: {str(e)}")
            raise UserError(_("Error connecting to OpenAI API: %s") % str(e))

import xmlrpc.client
import random

# ================= KONFIGURASI ODOO =================
URL = 'http://100.121.222.56:8069'
DB = 'ktt_restore'
USER = 'admin'
PASSWORD = 'admin'
# ====================================================

MODEL_NAME = 'crm.leads2'


def main():
    try:
        print(f"Mulai proses autentikasi ke database {DB}...")
        common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
        uid = common.authenticate(DB, USER, PASSWORD, {})

        if not uid:
            print("❌ Login gagal! Cek kembali konfigurasi Anda.")
            return

        print(f"✅ Login berhasil! UID: {uid}")
        models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

        # --- 1. SETUP RELATIONAL FIELDS ---
        print("\nMencari data pendukung (Country & Team)...")
        country_ids = models.execute_kw(DB, uid, PASSWORD, 'res.country', 'search', [[('name', 'ilike', 'Indonesia')]],
                                        {'limit': 1})
        country_id = country_ids[0] if country_ids else 1

        team_ids = models.execute_kw(DB, uid, PASSWORD, 'crm.team', 'search', [[('name', 'ilike', 'Dummy%')]],
                                     {'limit': 1})
        team_id = team_ids[0] if team_ids else 1

        # ⚠️ PENTING: UBAH 3 VARIABEL INI SESUAI DATABASE ANDA ⚠️
        CUSTOM_MODULE_ID = 1
        CUSTOM_INDUSTRY_ID = 1
        VALID_HOUR_GROUP = 'afternoon1130to1630'  # Ubah ke key selection yang valid (misal: '1', '08:00', 'morning', dll)

        # --- 2. SIAPKAN 10 DATA (DENGAN SKENARIO KEMIRIPAN) ---
        print("\nMenyiapkan 10 data random untuk testing Similar Leads...")

        # Skenario:
        # - 3 Lead dari PT Semesta Abadi (Mirip)
        # - 2 Lead dari PT Maju Jaya (Mirip)
        # - 2 Lead dari Toko Berkah (Mirip)
        # - 3 Lead Unik

        leads_data = [
            # Kelompok 1 (Mirip)
            {'name': 'Kebutuhan ERP Odoo', 'partner_name': 'PT Semesta Abadi'},
            {'name': 'Implementasi Modul Sales', 'partner_name': 'PT Semesta Abadi'},
            {'name': 'Tanya Harga Setup Odoo', 'partner_name': 'PT Semesta Abadi'},

            # Kelompok 2 (Mirip)
            {'name': 'Custom HRD System', 'partner_name': 'PT Maju Jaya'},
            {'name': 'Modul Payroll - Maju Jaya', 'partner_name': 'PT Maju Jaya'},

            # Kelompok 3 (Mirip)
            {'name': 'POS Kasir Cabang 1', 'partner_name': 'Toko Berkah'},
            {'name': 'POS Kasir Cabang 2', 'partner_name': 'Toko Berkah'},

            # Kelompok 4 (Unik)
            {'name': 'Website E-Commerce', 'partner_name': 'CV Budi Sentosa'},
            {'name': 'Sistem Inventory Gudang', 'partner_name': 'PT Angkasa Raya'},
            {'name': 'Accounting Setup', 'partner_name': 'PT Sejahtera Bersama'}
        ]

        # Menyuntikkan field mandatory lainnya ke dalam setiap data di atas
        for data in leads_data:
            data['country_id'] = country_id
            data['crm_module_id'] = CUSTOM_MODULE_ID
            data['industry_ai_id'] = CUSTOM_INDUSTRY_ID
            data['team_id'] = team_id
            data['hour_group'] = VALID_HOUR_GROUP

        # --- 3. EKSEKUSI INSERT DATA ---
        print(f"\nMemasukkan 10 Data ke model {MODEL_NAME}...\n")
        success_count = 0

        for idx, data in enumerate(leads_data, start=1):
            try:
                lead_id = models.execute_kw(DB, uid, PASSWORD, MODEL_NAME, 'create', [data])
                success_count += 1
                print(f"   ✅ [Lead {idx}] Berhasil dibuat: '{data['name']}' (Partner: {data['partner_name']})")
            except Exception as e:
                print(f"   ⚠️ [Lead {idx}] Gagal dibuat: {e}")
                break  # Stop loop jika ada error field mandatory agar terminal tidak spam

        if success_count == len(leads_data):
            print(f"\n🎉 SELESAI! {success_count} data berhasil dimasukkan.")
            print("Silakan jalankan ir.cron 'Similar Leads' Anda untuk melihat hasilnya.")
        else:
            print(f"\n❌ Selesai dengan error. Hanya {success_count}/10 data yang terbuat.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan fatal: {e}")


        # try:
        #     records.sync_master_sales_to_mln()
        # except Exception as err:
        #     _logger.exception('[KTT->MLN] Failed to sync on create: %s', err)
        #
        # return records

        # def write(self, vals):
        #     if vals.get('stage_id') == 37:
        #         vals['goingtomeetdate'] = fields.Datetime.now()
        #     # If this is a new record and team_id is being set but original_team_id isn't set yet
        #     if vals.get('team_id') and not self.original_team_id:
        #         vals['original_team_id'] = vals['team_id']
        #     # Never allow original_team_id to be set to False/None once it has a value
        #     elif 'original_team_id' in vals and not vals['original_team_id'] and self.original_team_id:
        #         vals.pop('original_team_id')
        #
        #     result = super(Leads2, self).write(vals)
        #
        #     if 'team_id' in vals or 'salesperson_ids' in vals:
        #         try:
        #             self.sync_master_sales_to_mln()
        #         except Exception as err:
        #             _logger.exception('[KTT->MLN] Failed to sync on write: %s', err)
        #
        #     return result

if __name__ == "__main__":
    main()
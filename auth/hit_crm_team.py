import xmlrpc.client

# ================= KONFIGURASI ODOO =================
URL = 'http://100.121.222.56:8069'
DB = 'ktt_restore'  # Menggunakan database baru Anda
USER = 'admin'  # Ganti dengan email/username login Anda
PASSWORD = 'admin'  # Ganti dengan password Anda


# ====================================================

def main():
    try:
        print("Mulai proses autentikasi ke database mln_new...")
        common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
        uid = common.authenticate(DB, USER, PASSWORD, {})

        if not uid:
            print("❌ Login gagal! Cek kembali konfigurasi Anda.")
            return

        print(f"✅ Login berhasil! UID: {uid}")
        models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

        # --- AMBIL COMPANY ID ---
        print("\nMengambil data Perusahaan (Company) user aktif...")
        user_data = models.execute_kw(DB, uid, PASSWORD, 'res.users', 'read', [[uid]], {'fields': ['company_id']})
        company_id = user_data[0]['company_id'][0]
        print(f"   ➜ Menggunakan Company ID: {company_id}")

        # --- CREATE CRM TEAM ---
        print("\nMembuat 10 Data CRM Team (Sales Team) dummy...")
        success_count = 0
        for i in range(20, 40):
            team_data = {
                'name': f'Dummy Sales Team {i}',
                'company_id': company_id
                # Anda juga bisa menambahkan field lain di sini jika butuh,
                # misalnya 'active': True
            }

            try:
                team_id = models.execute_kw(DB, uid, PASSWORD, 'crm.team', 'create', [team_data])
                success_count += 1
                print(f"   ➜ Berhasil membuat CRM Team: {team_data['name']} (ID: {team_id})")
            except Exception as e:
                print(f"⚠️ Gagal membuat CRM Team ke-{i}: {e}")
                break  # Berhenti jika ada field custom Equip3 yang ternyata mandatory

        if success_count > 0:
            print(f"\n🎉 SELESAI! {success_count} data dummy crm.team berhasil di-import.")
        else:
            print("\n❌ Gagal membuat CRM Team.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan fatal: {e}")


if __name__ == "__main__":
    main()
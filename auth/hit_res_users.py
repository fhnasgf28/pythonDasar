import xmlrpc.client

# ================= KONFIGURASI ODOO =================
URL = ''
DB = ''  # Database Anda
USER = ''  # Ganti dengan username login Anda
PASSWORD = ''  # Ganti dengan password Anda


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

        # --- CREATE USERS (SALESPERSON) ---
        print("\nMembuat 10 Data Salesperson (res.users) dummy...")
        success_count = 0
        for i in range(1, 11):
            user_values = {
                'name': f'Dummy Salesperson {i}',
                'login': f'sales{i}@dummy.com',  # Harus unik!
                'password': '123',  # Set password default agar mereka bisa login
                'company_id': company_id,  # Perusahaan utama
                # company_ids adalah Many2many, wajib pakai magic tuple (6, 0, [list_id])
                'company_ids': [(6, 0, [company_id])]
            }

            try:
                # Proses pembuatan user
                new_user_id = models.execute_kw(DB, uid, PASSWORD, 'res.users', 'create', [user_values])
                success_count += 1
                print(f"   ➜ Berhasil membuat User: {user_values['name']} (ID: {new_user_id})")
            except Exception as e:
                print(f"⚠️ Gagal membuat User ke-{i}: {e}")
                break  # Berhenti jika ada error (misal login sudah terpakai)

        if success_count > 0:
            print(f"\n🎉 SELESAI! {success_count} data dummy Salesperson berhasil di-import.")
            print("💡 Catatan: Semua user baru memiliki password '123'.")
        else:
            print("\n❌ Gagal membuat Salesperson.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan fatal: {e}")


if __name__ == "__main__":
    main()
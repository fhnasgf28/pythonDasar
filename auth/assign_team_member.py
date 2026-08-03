import xmlrpc.client
import random

# ================= KONFIGURASI ODOO =================
URL = 'http://100.121.222.56:8069'
DB = 'ktt_restore'
USER = 'admin'
PASSWORD = 'admin'


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

        # --- 1. CARI DATA DUMMY USERS ---
        print("\nMencari Dummy Salesperson...")
        # Kita cari user yang email/login-nya mengandung kata 'dummy.com'
        user_ids = models.execute_kw(DB, uid, PASSWORD, 'res.users', 'search', [[('login', 'ilike', '%@dummy.com')]])

        if not user_ids:
            print("⚠️ Tidak ada Dummy Salesperson yang ditemukan. Pastikan script pembuat user sudah dijalankan.")
            return
        print(f"   ➜ Ditemukan {len(user_ids)} Dummy Salesperson.")

        # --- 2. CARI DATA DUMMY CRM TEAM ---
        print("\nMencari Dummy CRM Team...")
        # Kita cari tim yang namanya mengandung kata 'Dummy'
        team_ids = models.execute_kw(DB, uid, PASSWORD, 'crm.team', 'search', [[('name', 'ilike', 'Dummy%')]])

        if not team_ids:
            print("⚠️ Tidak ada Dummy CRM Team yang ditemukan. Pastikan script pembuat tim sudah dijalankan.")
            return
        print(f"   ➜ Ditemukan {len(team_ids)} Dummy CRM Team.")

        # --- 3. PROSES PENGGABUNGAN (UPDATE / WRITE) ---
        print("\nMemulai proses assign anggota ke dalam tim...")
        success_count = 0

        for team_id in team_ids:
            # Pilih 2 sampai 4 user secara acak dari daftar user_ids untuk dimasukkan ke tim ini
            # Pastikan tidak melebihi jumlah total user yang ada
            jumlah_anggota = min(random.randint(2, 4), len(user_ids))
            selected_users = random.sample(user_ids, jumlah_anggota)

            # Di Odoo, mengupdate field Many2many (seperti member_ids)
            # dilakukan dengan magic tuple: (6, 0, [list_id_yang_mau_dimasukkan])
            update_data = {
                'member_ids': [(6, 0, selected_users)]
            }

            try:
                # Perhatikan: di sini kita menggunakan 'write', bukan 'create' karena datanya sudah ada
                models.execute_kw(DB, uid, PASSWORD, 'crm.team', 'write', [[team_id], update_data])
                success_count += 1
                print(f"   ➜ Berhasil memasukkan {len(selected_users)} anggota ke Tim (ID: {team_id})")
            except Exception as e:
                print(f"⚠️ Gagal update Tim (ID: {team_id}): {e}")

        if success_count > 0:
            print(f"\n🎉 SELESAI! {success_count} Tim berhasil diperbarui dengan anggota baru.")
        else:
            print("\n❌ Gagal melakukan proses penggabungan.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan fatal: {e}")


if __name__ == "__main__":
    main()
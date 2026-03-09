import xmlrpc.client
import json
import getpass
import sys


def main():
    print("=" * 45)
    print("   ODOO DATA IMPORTER - RES.COUNTRY.CITY")
    print("=" * 45)

    # --- 1. INPUT KREDENSIAL ---
    url = input("1. URL Odoo (cth: https://my-odoo.com): ").strip()
    if url.endswith('/'): url = url[:-1]

    db = input("2. Nama Database: ").strip()
    username = input("3. Email Login: ").strip()
    password = getpass.getpass("4. Password / API Key (Hidden): ").strip()

    filename = input("5. Nama file JSON (Default 'data_kota.json'): ").strip()
    if not filename:
        filename = 'data_kota.json'

    # --- 2. KONEKSI ---
    print("\n[INFO] Menghubungkan ke server...")
    try:
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})

        if not uid:
            print("[ERROR] Login Gagal! Cek kembali kredensial Anda.")
            return

        print(f"[SUKSES] Login berhasil (UID: {uid})")
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    except Exception as e:
        print(f"[ERROR] Koneksi bermasalah: {e}")
        return

    # --- 3. BACA DATA ---
    try:
        with open(filename, 'r') as file:
            cities_data = json.load(file)
            print(f"[INFO] Memuat {len(cities_data)} data dari file JSON.")
    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' tidak ditemukan.")
        return

    # --- 4. PERSIAPAN DATA (AUTO-SEARCH IDs) ---
    batch_data = []

    # Cari ID Negara Indonesia (Default)
    # Ubah 'Indonesia' jika nama negara di DB Anda berbeda
    print("[INFO] Mencari ID Negara 'Indonesia'...")
    country_ids = models.execute_kw(db, uid, password, 'res.country', 'search', [[['name', '=', 'Indonesia']]])
    country_id = country_ids[0] if country_ids else False

    if not country_id:
        print("[WARN] Negara 'Indonesia' tidak ditemukan. Field country_id akan kosong.")

    print("[INFO] Melakukan pencocokan Provinsi...")

    for item in cities_data:
        # Field dasar hanya nama
        vals = {
            'name': item['name'],
        }

        # Tambahkan country_id jika ada
        # if country_id:
        #     vals['country_id'] = country_id

        # Cari ID Provinsi (state_id) berdasarkan nama di JSON
        if 'province_name' in item:
            # Gunakan 'ilike' agar tidak case-sensitive
            state_ids = models.execute_kw(db, uid, password, 'res.country.state', 'search',
                                          [[['name', 'ilike', item['province_name']]]])

            if state_ids:
                vals['state_id'] = state_ids[0]  # Ambil ID pertama
            else:
                print(f"   -> [SKIP] Provinsi '{item['province_name']}' tidak ditemukan untuk kota {item['name']}.")

        batch_data.append(vals)

    # --- 5. EKSEKUSI ---
    if batch_data:
        print(f"\nSiap menembak {len(batch_data)} data ke model 'res.country.city'.")
        confirm = input("Lanjutkan? (y/n): ").lower()

        if confirm == 'y':
            try:
                # Perhatikan nama modelnya sudah diganti ke res.country.city
                new_ids = models.execute_kw(db, uid, password, 'res.country.city', 'create', [batch_data])
                print(f"\n[SELESAI] Sukses! {len(new_ids)} kota berhasil dibuat.")
            except xmlrpc.client.Fault as err:
                print(f"\n[ERROR ODOO] {err}")
                print("Tips: Pastikan model 'res.country.city' benar-benar ada di Odoo Anda.")
        else:
            print("\n[BATAL] Operasi dibatalkan.")
    else:
        print("\n[INFO] Data kosong atau tidak valid.")


if __name__ == '__main__':
    main()
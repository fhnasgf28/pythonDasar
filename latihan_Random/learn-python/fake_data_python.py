# latihan_Random/learn-python/hitung_jarak_tempuh.py

def hitung_jarak_tempuh(kota_asal, kota_tujuan, kecepatan):
    # jarak antara kota asal dan kota tujuan dalam km
    jarak = 0
    if kota_asal == "Jakarta" and kota_tujuan == "Bandung":
        jarak = 150
    elif kota_asal == "Jakarta" and kota_tujuan == "Surabaya":
        jarak = 700
    elif kota_asal == "Jakarta" and kota_tujuan == "Yogyakarta":
        jarak = 500
    elif kota_asal == "Bandung" and kota_tujuan == "Surabaya":
        jarak = 550
    elif kota_asal == "Bandung" and kota_tujuan == "Yogyakarta":
        jarak = 350
    elif kota_asal == "Surabaya" and kota_tujuan == "Yogyakarta":
        jarak = 250
    else:
        print("Kota tidak ditemukan")
        return

    # hitung waktu yang dibutuhkan
    waktu = jarak / kecepatan

    return waktu


if __name__ == "__main__":
    print("Contoh penggunaan:")
    print(hitung_jarak_tempuh("Jakarta", "Bandung", 60))
    print(hitung_jarak_tempuh("Jakarta", "Surabaya", 60))
    print(hitung_jarak_tempuh("Jakarta", "Yogyakarta", 60))
    print(hitung_jarak_tempuh("Bandung", "Surabaya", 60))
    print(hitung_jarak_tempuh("Bandung", "Yogyakarta", 60))
    print(hitung_jarak_tempuh("Surabaya", "Yogyakarta", 60))
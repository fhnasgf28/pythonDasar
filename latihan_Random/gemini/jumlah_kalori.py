kalori_makanan  = {
    "Nasi Putih" : 1300,
    "ayam goreng": 200,
    "sayur asem": 30,
    "buah apel": 52
}

def hitung_kalori(makanan, porsi):
    kalori_per_100g = kalori_makanan.get(makanan.lower(), 0)
    total_kalori = kalori_per_100g * porsi / 100
    return total_kalori

# contoh penggunaan
makanan = "Ayam Goreng"
porsi = 150
total_kalori = hitung_kalori(makanan, porsi)
print(f"Kalori dalam {porsi} gram {makanan}: {total_kalori} kalori")

# menghitung waktu kredit motor

def hitung_waktu_kredit(harga_motor, uang_muka, bunga, angsuran):
    sisa_harga = harga_motor - uang_muka
    bunga_perbulan = (bunga / 100) / 12
    total_angsuran = sisa_harga / (1 - (1 + bunga_perbulan) ** (-angsuran))
    angsuran_bulanan = total_angsuran / angsuran
    print(f"Angsuran Bulanan : Rp {angsuran_bulanan: ,}")

    print(f"Lama kredit: {angsuran} bulan")

# Contoh penggunaan
harga_motor = 20000000
uang_muka = 5000000
bunga = 10
angsuran = 36
hitung_waktu_kredit(harga_motor, uang_muka, bunga, angsuran)

def hitung_masa_subur(panjang_siklus):
    hari_pertama_menstruasi = 1
    hari_ovulasi = hari_pertama_menstruasi + 14
    awal_masa_subur = hari_ovulasi - 5
    akhir_masa_subur = hari_ovulasi + 5
    print(f"Masa subur diperkirakan antara hari ke-{awal_masa_subur} hingga {akhir_masa_subur}")

panjang_siklus = 28
hitung_masa_subur(panjang_siklus)
def hitung_suara(data_suara):
    """
    Fungsi untuk menghitung jumlah suara dari setiap daerah

    """

    pemenang = ""
    jumlah_suara_terbanyak = 0
    for kandidat, suara in data_suara.items():
        if suara > jumlah_suara_terbanyak:
            pemenang = kandidat
            jumlah_suara_terbanyak = suara
    return pemenang

# contoh penggunaan 
tata_suara = {
    "Kota A": 100,
    "Kota B": 200,
    "Kota C": 150,
    "Kota D": 250,
    "Kota E": 300,
    "Kota F": 180,
    "Kota G": 220,
    "Kota H": 90,
    "Kota I": 400,
    "Kota J": 140,
    "Kota K": 170,
    "Kota L": 350,
    "Kota M": 50,
    "Kota N": 275
}

pemenang = hitung_suara(tata_suara)
print(f"Pemenang adalah {pemenang}")
def hitung_bunga():
    investasi_awal = float(input("Masukkan jumlah investasi awal: "))
    tingkat_bunga = float(input("Masukkan tingkat bunga per tahun (dalam persen): "))
    tahun_investasi = int(input("Masukkan jumlah tahun investasi: "))

    bunga = investasi_awal * (tingkat_bunga / 100) * tahun_investasi
    print("Bunga yang diperoleh setelah {} tahun adalah: {}".format(tahun_investasi, bunga))

hitung_bunga()
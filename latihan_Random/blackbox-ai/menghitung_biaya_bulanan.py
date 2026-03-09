def hitung_biaya_bulanan():
    kategori_pengeluaran = {}
    jumlah_bulan = int(input("Masukan Jumlah Bulan : "))

    while True:
        nama_kategori = input("Masukan nama kategori pengeluaran (atau 'selesai' untuk berhenti):")
        if nama_kategori.lower() == 'selesai':
            break
        jumlah_pengeluaran = float(input("Masukan jumlah pengeluaran untuk {}: ".format(nama_kategori)))
        kategori_pengeluaran[nama_kategori] = jumlah_pengeluaran

    total_biaya_bulanan = {}
    for kategori, pengeluaran in kategori_pengeluaran.items():
        total_biaya_bulanan[kategori] = pengeluaran * jumlah_bulan

    total_biaya_bulanan_keseluruhan = sum(total_biaya_bulanan.values())

    print("Total biaya bulanan untuk setiap kategori:")
    for kategori, biaya in total_biaya_bulanan.items():
        print("{}: {}".format(kategori, biaya))

    print("Total biaya bulanan keseluruhan: {}".format(total_biaya_bulanan_keseluruhan))

hitung_biaya_bulanan()
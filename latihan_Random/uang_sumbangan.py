def hitung_sumbangan(harga_barang, jumlah_donatur):
    if jumlah_donatur == 0:
        return "Jumlah donatur harus lebih besar dari 0"
    return harga_barang / jumlah_donatur

harga_jam_dinding = 2000000
jumlah_donatur = 100

sumbangan_per_orang = hitung_sumbangan(harga_jam_dinding, jumlah_donatur)
print(sumbangan_per_orang)
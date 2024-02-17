jumlah_barang = 24
jumlah_barang_dalam_lusin = jumlah_barang / 12

if jumlah_barang_dalam_lusin % 1 == 0:
    jumlah_barang_dalam_lusin = int(jumlah_barang_dalam_lusin)

print(f"{jumlah_barang} buah, totalnya {jumlah_barang_dalam_lusin} lusin")

# kesatuan kodi
jumlah_barang = 60
jumlah_barang_dalam_kodi = jumlah_barang / 20

# konversi x.0 menjadi x

if jumlah_barang_dalam_kodi % 1 == 0:
    jumlah_barang_dalam_kodi = int(jumlah_barang_dalam_kodi)

print(f"{jumlah_barang} buah, totalnya {jumlah_barang_dalam_kodi} kodi")
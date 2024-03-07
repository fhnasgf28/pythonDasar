''' latihan Kwargs'''

# menjumlahkan semua argument yang dimasukan

def argument(*args):
    total = 0
    for org in args:
        total += org
    return total

print(argument(1,2,3,4,5))


# menyapa seseorang dengan nama gelar

def sapa(nama, **kwargs):
    gelar = kwargs.get("gelar", "")
    return f"Halo {gelar} {nama}"

print(sapa("Budi"))
print(sapa("Budi", gelar="Dr."))

# mencetak informasi buku
def cetak_info_buku(judul, penulis, **kwargs):
    tahun_terbit = kwargs.get("tahun_terbit", None)
    if tahun_terbit is not None:
        print(f"Judul\t: {judul}")
        print(f"Penulis \t: {penulis}")
        print(f"Tahun Terbit\t: {tahun_terbit}")
    else:
        print(f"Judul {judul}")
        print(f"Penulis\t:{penulis}")

cetak_info_buku("Laskar Pelangi", "Andrea Hirata")
cetak_info_buku("Laskar Pelangi", "Andrea Hirata", tahun_terbit=2005)

# mencetak informasi produk
def cetak_informasi_produk(nama_produk, harga, **kwargs):
    kategori = kwargs.get("Kategori", "Lainnya")
    print(f"Harga\t: Rp{harga}")
    print(f"Nama Produk\t: {nama_produk}")
    print(f"Kategori\t:{kategori}")

cetak_informasi_produk("Sepatau", 100000)
cetak_informasi_produk("Sepatu",10000, kategori="Fashion")

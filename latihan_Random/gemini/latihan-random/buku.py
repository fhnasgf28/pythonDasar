class Buku:
    def __init__(self, judul, penulis, isbn):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"ISBN: {self.isbn}")


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku {buku.judul} berhasil ditambahkan ke perpustakaan")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                return buku
        return None

    def tampilkan_semua_buku(self):
        print(f"Daftar Buku di Perpustakaan {self.nama}")
        for buku in self.daftar_buku:
            print(f"Judul: {buku.judul}")
            print(f"Penulis: {buku.penulis}")
            print(f"ISBN: {buku.isbn}")
            print("")
        if not self.daftar_buku:
            print("Perpustakaan ini belum memiliki buku")

# contoh penggunaan
perpustakaan = Perpustakaan("Perpustakaan Umum")

buku1 = Buku("Belajar Python", "Farhan", "123456")
buku2 = Buku("Belajar Java", "Ucup", "7891011")
buku3 = Buku("Belajar C++", "Budi", "12131415")
buku4 = Buku("Belajar PHP", "Joko", "16171819")

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)
perpustakaan.tambah_buku(buku4)

perpustakaan.tampilkan_semua_buku()

buku_dicari = perpustakaan.cari_buku("Belajar Python")
if buku_dicari:
    print("Buku ditemukan:")
    buku_dicari.tampilkan_info()
else:
    print("Buku tidak ditemukan")
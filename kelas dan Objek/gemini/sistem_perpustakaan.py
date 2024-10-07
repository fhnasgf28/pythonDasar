class Buku:
    def __init__(self, judul, penulis, isbn, jumlah_eksamplar):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.jumlah_eksamplar = jumlah_eksamplar


class Peminjam:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon


class Peminjaman:
    def __init__(self, buku, peminjam, tanggal_pinjam, tanggal_jatuh_tempo, status):
        self.buku = buku
        self.peminjam = peminjam
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_jatuh_tempo = tanggal_jatuh_tempo
        self.status = status


# implementasi
buku1 = Buku("Buku 1", "Penulis ", "34534-43345-3434", 5)
peminjam1 = Peminjam("Budi", "Jl.Sudirman 12", "8786872334")

print(f"Judul buku\t:{buku1.judul}")
print(f"Penulis buku\t:{buku1.penulis}")
print(f"ISBN buku\t:{buku1.isbn}")
print(f"Jumlah eksamplar buku\t:{buku1.jumlah_eksamplar}")

print(f"Nama peminjam: {peminjam1.nama}")  # Output: Nama peminjam: Budi
print(f"Alamat peminjam: {peminjam1.alamat}")  # Output: Alamat peminjam: Jl.Sudirman 12
print(f"Nomor telepon peminjam: {peminjam1.nomor_telepon}")  # Output: Nomor telepon peminjam: 8786872334

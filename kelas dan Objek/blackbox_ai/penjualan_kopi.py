class ProdukKopi:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class PenjualanKopi:
    def __init__(self):
        self.daftar_produk = []
        self.total_penjualan = 0

    def tambah_produk(self, nama, harga):
        produk = ProdukKopi(nama, harga)
        self.daftar_produk.append(produk)
        print(f"Produk {nama} telah ditambahkan")

    def tampilkan_daftar_produk(self):
        print("Daftar Produk Kopi:")
        for i, produk in enumerate(self.daftar_produk, start=1):
            print(f"{i}. {produk.nama} - Rp {produk.harga}")

    def beli_kopi(self, nama_produk, jumlah):
        for produk in self.daftar_produk:
            if produk.nama == nama_produk:
                total_harga = produk.harga * jumlah
                self.total_penjualan += total_harga
                print(f"Anda telah membeli {jumlah} {nama_produk} seharga Rp {total_harga}.")
                return
        print("Produk tidak ditemukan.")

    def tampilkan_total_penjualan(self):
        print(f"Total Penjualan: Rp {self.total_penjualan}")

# buat objek penjualan KOpi
penjualan_kopi = PenjualanKopi()

# tambahkan produk kopi
penjualan_kopi.tambah_produk("Kopi Hitam", 10000)
penjualan_kopi.tambah_produk("Kopi susu", 150000)
penjualan_kopi.tambah_produk("Kopi Capuccino", 20000)

# tampilkan daftar produk kopi
penjualan_kopi.tampilkan_daftar_produk()

# Beli KOpi
penjualan_kopi.beli_kopi("Kopi Hitam", 2)
penjualan_kopi.beli_kopi("Kopi Susu", 1)

# tampilkan total penjualan
penjualan_kopi.tampilkan_total_penjualan()
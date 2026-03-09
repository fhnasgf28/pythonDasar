class Produk:
    def __init__(self, nama, harga, jumlah_terjual):
        self.nama = nama 
        self.harga = harga
        self.jumlah_terjual = jumlah_terjual
    
    def hitung_total(self):
        return self.harga * self.jumlah_terjual

class Transaksi:
    def __init__(self):
        self.daftar_produk = []
    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
    def hitung_total_penjualan(self):
        total = 0 
        for product in self.daftar_produk:
            total += product.hitung_total()
        return total
    def tampilkan_detail_transaksi(self):
        print("Detail Transaksi:")
        for produk in self.daftar_produk:
            print(f"{produk.nama} - Harga: Rp{produk.harga:,} - Terjual: {produk.jumlah_terjual} - Total: Rp{produk.hitung_total():,}")
        print(f"\nTotal Penjualan: Rp{self.hitung_total_penjualan():,}")
# Program Utama
if __name__ == "__main__":
    # Membuat objek transaksi
    transaksi = Transaksi()

    # Input data produk dari pengguna
    while True:
        nama = input("Masukkan nama produk (atau 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break

        try:
            harga = int(input("Masukkan harga produk: "))
            jumlah_terjual = int(input("Masukkan jumlah terjual: "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue

        product = Produk(nama, harga, jumlah_terjual)
        transaksi.tambah_produk(product)
    
    transaksi.tampilkan_detail_transaksi()

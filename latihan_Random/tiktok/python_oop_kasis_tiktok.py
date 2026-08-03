# entitas produk, pelanggan, kasir
# produk 

class Produk:
    """mewakili barang/ produk yang dijual mamang toko"""
    def __init__(self, nama_produk, harga_produk):
        self.nama_produk = nama_produk
        self.harga_produk = harga_produk

    def tampilkan_info(self):
        print(f"Nama produk: {self.nama_produk}, Harga Produk: {self.harga_produk}")

class Pelanggan:
    """mewakili pelanggan yang membeli produk"""
    def __init__(self, nama_pelanggan, is_member=False):
        self.nama_pelanggan = nama_pelanggan
        self.is_member = is_member
    
    def get_diskon_member(self):
        return 0.5 if self.is_member else 0.0

class Kasir: 
    """Mengelola transaksi, keranjang belanja, dan cetak struk"""
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.keranjang = []
    
    def tambah_ke_keranjang(self, produk, jumlah):
        self.keranjang.append({"produk": produk, "jumlah": jumlah})
        print(f"{jumlah} {produk.nama_produk} telah ditambahkan ke keranjang.")
    Produk
    def hitung_total(self):
        subtotal = sum(item["produk"].harga_produk * item["jumlah"] for item in self.keranjang)
        diskon_promo = 0.10 if subtotal > 100000 else 0.0 
        # diskon tambahan untuk member 
        diskon_member = self.pelanggan.get_diskon_member()
        print(diskon_member)
        total_diskon_rate = diskon_promo + diskon_member
        nominal_diskon = subtotal * total_diskon_rate
        total_akhir = subtotal - nominal_diskon
        return subtotal, nominal_diskon, total_akhir

    def cetak_struk(self):
        subtotal, nominal_diskon, total_akhir = self.hitung_total()
        print("\n=== STRUK BELANJA ===")
        print(f"Pelanggan: {self.pelanggan.nama_pelanggan}")
        for item in self.keranjang:
            produk = item["produk"]
            jumlah = item["jumlah"]
            print(f"{produk.nama_produk} x {jumlah} = {produk.harga_produk * jumlah}")
        print(f"Subtotal: {subtotal}")
        print(f"Diskon: {nominal_diskon}")
        print(f"Total Akhir: {total_akhir}")

def main():
    # membuat produk
    produk1 = ("Buku", 50000)
    produk2 = Produk("Pulpen", 10000)
    produk3 = Produk("Penghapus", 5000)

    # membuat pelanggan
    pelanggan1 = Pelanggan("Andi", is_member=True)
    pelanggan2 = Pelanggan("Budi", is_member=False)

    # membuat kasir untuk pelanggan1
    kasir1 = Kasir(pelanggan1)
    kasir1.tambah_ke_keranjang(produk1, 2)  # 2 Buku
    kasir1.tambah_ke_keranjang(produk2, 5)  # 5 Pulpen
    kasir1.cetak_struk()

    print("\n")

    # membuat kasir untuk pelanggan2
    kasir2 = Kasir(pelanggan2)
    kasir2.tambah_ke_keranjang(produk3, 10)  # 10 Penghapus
    kasir2.cetak_struk()

if __name__ == "__main__":
    main()
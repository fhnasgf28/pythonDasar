class Product:
    def __init__(self, nama, harga, stok):
        self.nama = nama 
        self.harga = harga 
        self.stok = stok
        print(f"nama: {self.nama} | Harga: Rp{self.harga:,.2f} stock {self.stok}")
    
    def tambah_stock(self, jumalah):
        if jumalah > 0:
            self.stok += jumalah
            print(f"Stock {self.nama} bertambah {jumlah}")
        else:
            print("jumlah penambahan stok harus positif")
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama} | Harga: Rp{self.harga:,.2f} | stok: {self.stok}")

    def kurangi_stok(self, jumlah):
        if jumlah > 0:
            if self.stok >= jumlah:
                self.stok -= jumlah
                print(f"stok {self.nama} berkurang {jumlah} stok baru: {self.stok}")
            else:
                print(f"Error:Stok {self.nama} tidak cukup, tersisa {self.stok}")
        else:
            print("jumlah pengurangan stok harus positif")

# contoh penggunaan 
print("-------Mengelola Inventaris----------")
laptop = Product("Laptop ASUS", 125000000, 10)
mouse = Product("Mouse Logitech", 1500000, 90)
keyboard = Product("Keyboard Mekanik", 750000, 50)
inventaris_barang = [laptop, mouse, keyboard]

print("\n-- inventaris saat ini ----")
for barang in inventaris_barang:
    barang.tampilkan_info()
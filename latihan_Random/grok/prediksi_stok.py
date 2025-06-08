class PenjualanHarian:
    def __init__(self, nanam_produk):
        self.__nama_produk = nanam_produk
        self.__data_penjualan = []

    def tambah_penjualan(self, jumlah):
        if jumlah >= 0:
            self.__data_penjualan.append(jumlah)
            print(f"Penjualan {self.__nama_produk} sejumlah {jumlah} berhasil ditambahkan.")
        else:
            print("Jumlah penjualan harus lebih besar atau sama dengan 0.")

    def hitung_rata_rata(self):
        """Menghitung rata rata penjualan harian"""
        if len(self.__data_penjualan) == 0:
            return 0
        return sum(self.__data_penjualan) / len(self.__data_penjualan)

    def get_nama_produk(self):
        return self.__nama_produk

    def get_data_penjualan(self):
        return self.__data_penjualan

class PrediksiStok:
    def __init__(self, penjualan, faktor_keamanan=1.2):
        self.__penjualan = penjualan
        self.__faktor_keamanan = faktor_keamanan

    def prediksi_mingguan(self):
        rata_rata_harian = self.__penjualan.hitung_rata_rata()
        prediksi = rata_rata_harian * 7 *self.__faktor_keamanan
        return round(prediksi)

    def tampilkan_laporan(self):
        """Menampilkan laporan prediksi stok"""
        prediksi = self.prediksi_mingguan()
        print(f"\nLaporan Prediksi Stok untuk {self.__penjualan.get_nama_produk()}:")
        print(f"Data penjualan harian: {self.__penjualan.get_data_penjualan()}")
        print(f"Rata-rata penjualan harian: {self.__penjualan.hitung_rata_rata():.2f} unit")
        print(f"Prediksi stok mingguan (dengan faktor keamanan {self.__faktor_keamanan}): {prediksi} unit")


# Program Utama
def main():
    # Membuat objek untuk produk "Roti Coklat"
    roti_coklat = PenjualanHarian("Roti Coklat")

    # Menambahkan data penjualan harian (contoh 5 hari)
    roti_coklat.tambah_penjualan(10)
    roti_coklat.tambah_penjualan(15)
    roti_coklat.tambah_penjualan(12)
    roti_coklat.tambah_penjualan(8)
    roti_coklat.tambah_penjualan(14)

    # Membuat objek prediksi stok
    prediksi_roti = PrediksiStok(roti_coklat, faktor_keamanan=1.2)

    # Menampilkan laporan
    prediksi_roti.tampilkan_laporan()


if __name__ == "__main__":
    main()
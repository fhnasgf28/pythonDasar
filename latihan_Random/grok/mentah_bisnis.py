class KeuanganBisnis:
    def __init__(self):
        self.__pendapatan = []  # List privat untuk pendapatan
        self.__pengeluaran = []  # List privat untuk pengeluaran

    def tambah_pendapatan(self, jumlah):
        """Menambahkan pendapatan ke daftar"""
        if jumlah >= 0:
            self.__pendapatan.append(jumlah)
            print(f"Pendapatan Rp {jumlah:,} ditambahkan.")
        else:
            print("Pendapatan tidak boleh negatif!")

    def tambah_pengeluaran(self, jumlah):
        """Menambahkan pengeluaran ke daftar"""
        if jumlah >= 0:
            self.__pengeluaran.append(jumlah)
            print(f"Pengeluaran Rp {jumlah:,} ditambahkan.")
        else:
            print("Pengeluaran tidak boleh negatif!")

    def hitung_total_pendapatan(self):
        """Menghitung total pendapatan"""
        return sum(self.__pendapatan) if self.__pendapatan else 0

    def hitung_total_pengeluaran(self):
        """Menghitung total pengeluaran"""
        return sum(self.__pengeluaran) if self.__pengeluaran else 0

    def hitung_keuntungan(self):
        """Menghitung keuntungan bersih"""
        return self.hitung_total_pendapatan() - self.hitung_total_pengeluaran()

    def hitung_margin(self):
        """Menghitung margin keuntungan dalam persen"""
        total_pendapatan = self.hitung_total_pendapatan()
        keuntungan = self.hitung_keuntungan()
        if total_pendapatan > 0:
            return (keuntungan / total_pendapatan) * 100
        return 0


class LaporanKeuangan:
    def __init__(self, keuangan, tarif_pajak=0.1):
        self.__keuangan = keuangan  # Objek KeuanganBisnis
        self.__tarif_pajak = tarif_pajak  # Misal 10% pajak dari keuntungan

    def hitung_pajak(self):
        """Menghitung pajak dari keuntungan"""
        keuntungan = self.__keuangan.hitung_keuntungan()
        if keuntungan > 0:
            return keuntungan * self.__tarif_pajak
        return 0

    def tampilkan_laporan(self):
        """Menampilkan laporan keuangan lengkap"""
        total_pendapatan = self.__keuangan.hitung_total_pendapatan()
        total_pengeluaran = self.__keuangan.hitung_total_pengeluaran()
        keuntungan = self.__keuangan.hitung_keuntungan()
        margin = self.__keuangan.hitung_margin()
        pajak = self.hitung_pajak()

        print("\n=== Laporan Keuangan Bisnis ===")
        print(f"Total Pendapatan: Rp {total_pendapatan:,}")
        print(f"Total Pengeluaran: Rp {total_pengeluaran:,}")
        print(f"Keuntungan Bersih: Rp {keuntungan:,}")
        print(f"Margin Keuntungan: {margin:.2f}%")
        if pajak > 0:
            print(f"Pajak ({self.__tarif_pajak*100}% dari keuntungan): Rp {pajak:,}")
            print(f"Keuntungan Setelah Pajak: Rp {keuntungan - pajak:,}")


# Program Utama
def main():
    bisnis = KeuanganBisnis()
    laporan = LaporanKeuangan(bisnis, tarif_pajak=0.1)

    while True:
        print("\nMenu Kalkulator Keuntungan Bisnis:")
        print("1. Tambah Pendapatan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Laporan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            try:
                jumlah = float(input("Masukkan jumlah pendapatan (Rp): "))
                bisnis.tambah_pendapatan(jumlah)
            except ValueError:
                print("Masukkan angka yang valid!")
        elif pilihan == "2":
            try:
                jumlah = float(input("Masukkan jumlah pengeluaran (Rp): "))
                bisnis.tambah_pengeluaran(jumlah)
            except ValueError:
                print("Masukkan angka yang valid!")
        elif pilihan == "3":
            laporan.tampilkan_laporan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan kalkulator!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")


if __name__ == "__main__":
    main()
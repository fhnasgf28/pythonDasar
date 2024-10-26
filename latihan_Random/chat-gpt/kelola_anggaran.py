class Anggaran:
    def __init__(self):
        self.pemasukan = 0
        self.pengeluaran = 0

    def tambah_pemasukan(self, jumlah):
        self.pemasukan += jumlah
        print(f"Pemasukan ditambahkan: {jumlah}")

    def tambah_pengeluaran(self, jumlah):
        self.pengeluaran += jumlah
        print(f"Pengeluaran ditambahkan: {jumlah}")

    def saldo_akhir(self):
        return self.pemasukan - self.pengeluaran

def main():
    anggaran = Anggaran()
    while True:
        print("\n1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Saldo Akhir")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            jumlah = float(input("Masukkan jumlah pemasukan: "))
            anggaran.tambah_pemasukan(jumlah)
        elif pilihan == '2':
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            anggaran.tambah_pengeluaran(jumlah)
        elif pilihan == '3':
            print(f"Saldo Akhir: {anggaran.saldo_akhir()}")
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak dikenal. Silakan coba lagi.")

if __name__ == "__main__":
    main()
class Dzikir:
    def __init__(self, teks, kategori, keutamaan=""):
        self.teks = teks
        self.kategori = kategori
        self.keutamaan = keutamaan

    def tampilkan_dzikir(self):
        print(f"Dzikir {self.kategori}")
        print(f"Keutamaan: {self.keutamaan}")
        print(f"{self.teks}\n")
        if self.keutamaan:
            print(f"Keutamaan: {self.keutamaan}")

class KumpulanDzikir:
    def __init__(self, nama):
        self.daftar_dzikir = []
        self.nama = nama

    def tambah_dzikir(self, dzikir):
        self.daftar_dzikir.append(dzikir)
        print(f"Dzikir {dzikir.kategori} berhasil ditambahkan ke kumpulan dzikir {self.nama}")

    def tampilkan_dzikir_berdasarkan_kategori(self, kategori):
        print(f"tampilkan dzikir berdasarkan kategori {kategori.capitalize()}")
        for dzikir in self.daftar_dzikir:
            if dzikir.kategori == kategori:
                dzikir.tampilkan_dzikir()

    def tampilkan_semua_dzikir(self):
        print(f"Kumpulan Dzikir {self.nama}")
        for dzikir in self.daftar_dzikir:
            dzikir.tampilkan_dzikir()
# contoh penggunaan
kumpulan_dzikir = KumpulanDzikir("Dzikir Harian")

dzikir1 = Dzikir("Subhanallah", "pagi", "Mendapat pahala sebanyak orang yang mengucapkan dzikir tersebut")
dzikir2 = Dzikir("Alhamdulillah", "pagi", "Mendapat pahala sebanyak orang yang mengucapkan dzikir tersebut")
dzikir3 = Dzikir("Allahu Akbar", "pagi", "Mendapat pahala sebanyak orang yang mengucapkan dzikir tersebut")
dzikir4 = Dzikir("La ilaha illallah", "pagi", "Mendapat pahala sebanyak orang yang mengucapkan dzikir tersebut")
dzikir5 = Dzikir("Astaghfirullah", "pagi", "Mendapat pahala sebanyak orang yang mengucapkan dzikir tersebut")

kumpulan_dzikir.tambah_dzikir(dzikir1)
kumpulan_dzikir.tambah_dzikir(dzikir2)
kumpulan_dzikir.tambah_dzikir(dzikir3)
kumpulan_dzikir.tambah_dzikir(dzikir4)
kumpulan_dzikir.tambah_dzikir(dzikir5)

kumpulan_dzikir.tampilkan_dzikir_berdasarkan_kategori("pagi")
kumpulan_dzikir.tampilkan_semua_dzikir()

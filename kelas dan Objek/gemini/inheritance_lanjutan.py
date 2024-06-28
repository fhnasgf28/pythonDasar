class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan")


class Mamalia(Binatang):
    def melahirkan(self):
        print(f"{self.nama} melahirkan anaknya")


class Burung(Binatang):
    def terbang(self):
        print(f"{self.nama} sedang terbang")


kucingku = Mamalia("Kucing")
kucingku.makan()
kucingku.melahirkan()

burungku = Burung("Burung Hantu")
burungku.makan()
burungku.terbang()

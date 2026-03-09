class BangunDatar:
    def __init__(self, lebar, tinggi):
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_luas(self):
        pass


class PersegiPanjang(BangunDatar):
    def hitung_luas(self):
        return self.lebar * self.tinggi


class Segitigaku(BangunDatar):
    def hitung_luas(self):
        return 0.5 * self.lebar * self.tinggi


persegipanjang = PersegiPanjang(10, 5)
print(f"Luas persegi panjang: {persegipanjang.hitung_luas()}")

segitigaku = Segitigaku(6, 8)
print(f"Luas segitiga: {segitigaku.hitung_luas()}")
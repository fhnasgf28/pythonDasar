class Handphone:
    def __init__(self, harga, masa_pakai, penggunaan_untuk_kerja):
        self.harga = harga
        self.masa_pakai = masa_pakai
        self.penggunaan_untuk_kerja = penggunaan_untuk_kerja

    def hitung_biaya_perbulan(self):
        if self.penggunaan_untuk_kerja:
            return self.harga / (self.masa_pakai * 12 * 1.5)
        else:
            return self.harga / (self.masa_pakai * 12 * 0.8)

    def __str__(self):
        return f"Handphone dengan harga Rp {self.harga}, masa pakai {self.masa_pakai} tahun, dan penggunaan untuk kerja {self.penggunaan_untuk_kerja}"

def main():
    hp = Handphone(5000000, 8, True)
    print(hp)
    print(f"Biaya per bulan: Rp {hp.hitung_biaya_perbulan():,.0f}")

if __name__ == "__main__":
    main()

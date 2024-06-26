class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def start(self):
        print(f"Mobil {self.merk} {self.warna} tahun {self.tahun} dinyalakan")

    def stop(self):
        print(f"Mobil {self.merk} {self.warna} tahun {self.tahun} dimatikan")


mobilkua = Mobil("Toyota", "Merah", 2020)
mobilkua.start()
print(f"Merk Mobil: {mobilkua.merk}")
mobilkua.stop()

class Kendaraan:
    def berjalan(self):
        print("Berjalan1...")

class Mobil(Kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        super().berjalan()
        print(f"Berjalan Dengan Cepat...{kecepatan}{satuan}")

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan(150)
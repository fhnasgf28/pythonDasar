class Mahasiswa:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"Perkenalkan saya {self.nama} dari {self.asal}")

# contoh penggunaan
mhs = Mahasiswa(nama='John', asal="Jakarta")
mhs.perkenalan()
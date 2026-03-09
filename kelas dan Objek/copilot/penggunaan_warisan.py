class Mahasiswa:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"Perkenalkan saya {self.nama} dari {self.asal}")


# contoh penggunaan
mhs = Mahasiswa(nama='John', asal="Jakarta")
mhs.perkenalan()


class Dosen(Mahasiswa):
    def __init__(self, nama, asal, mata_kuliah):
        super().__init__(nama, asal)
        self.mata_kuliah = mata_kuliah

    def ajar(self):
        print(f"saya mengajar mata kuliah {self.mata_kuliah}")

        # contoh penggunaan


dosen = Dosen(nama='prof. smith', asal='bandung', mata_kuliah='Pemrograman')
dosen.perkenalan()
dosen.ajar()

# membuat kelas Mahasiswa
class Mahasiswa:
    nama = None
    asal = None

    def perkenalan(self):
        print(f"Perkenalkan saya {self.nama} dari {self.asal}")


deni = Mahasiswa()
deni.nama = "Deni"
deni.asal = "Jawa Timur"

lendis = Mahasiswa()
lendis.nama = "Lendis"
lendis.asal = "Jawa Tengah"

# panggil fungsi perkenalan
deni.perkenalan()
lendis.perkenalan()

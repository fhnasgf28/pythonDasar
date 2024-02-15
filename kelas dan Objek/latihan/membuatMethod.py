class Mahasiswa():
    nama = "nama"

    def belajar(self):
        print(f"{self.nama} sedang belajar")


otong = Mahasiswa()
ucup = Mahasiswa()

otong.nama = "otong"
ucup.nama = "suracup"

otong.belajar()
ucup.belajar()

class Mahasiswa():
    def __init__(self, inputNama, inputNIM):
        self.nama = inputNama
        self.nim = inputNIM
    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)
    def tidur(self):
        print(self.nama, "sedang tidur")

otong = Mahasiswa("otong surotong", 89796796)

print(otong.nim)
print(otong.nama)



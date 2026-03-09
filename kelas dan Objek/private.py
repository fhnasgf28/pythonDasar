class Mahasiswa():
    jurusan = "Informatika"
    __nilai = 0 # private

    def __init__(self, inputNama, input_nim):
        self.nama = inputNama
        self.nim = input_nim

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai
    def check_status(self):
        if self.__nilai >= 70:
            print(self.nama,"Lulus")
        else:
            print(self.nama,"Tidak Lulus")
# main program
otong = Mahasiswa("otong surotong", 89796796)
ucup = Mahasiswa("ucup surucup", 12345678)

otong.uts(20)
otong.uas(90)
otong.check_status()
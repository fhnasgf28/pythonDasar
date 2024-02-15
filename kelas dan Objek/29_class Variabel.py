class Mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self,inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        Mahasiswa.jumlah_mahasiswa += 1

# main programmnya
otong = Mahasiswa("otong surotong", 89796796)
ucup = Mahasiswa("ucup surucup", 12345678)
casandra_huleng = Mahasiswa("casandra huleng", 123454353678)

print(Mahasiswa.jumlah_mahasiswa)
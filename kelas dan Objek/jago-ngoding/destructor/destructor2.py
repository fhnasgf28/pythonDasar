class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        print(f'mahasiswa {self.nama} dibuat')

    def __del__(self):
        print(f'Mahasiswa {self.nama} dihapus')


mahasiswaX = Mahasiswa('budi')
mahasiswaX = 10

print(f'mahasiswa = {mahasiswaX}')

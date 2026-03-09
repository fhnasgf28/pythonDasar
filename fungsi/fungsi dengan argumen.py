# fungsi dengan argument
def hello_world(nama):
    ''' fungsi hello world menerima input dengan variabel nama'''
    print(f'selamat datang dunia wahay {nama}')


hello_world('farhan')
hello_world('assegaf')

# program tambah
def tambah(angka_1, angka_2):
    """ fungsi tambah menerima input angka 1 dan angka 2"""
    hasil = angka_1 + angka_2
    print(f'hasilanya {angka_1} + {angka_2} = {hasil}')

tambah(1, 2)
tambah(3, 4)

def say_hi(list_mahasiswa):
    """fungsi say hi menerima input list mahasiswa"""
    for mahasiswa in list_mahasiswa:
        print(f'halo {mahasiswa}')

say_hi(['farhan', 'assegaf', 'farhan'])

def say_hi1(list_peserta):
    """fungsi say hi menerima input list peserta"""
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'halo {peserta}')

anggota_boyband = ['farhan', 'assegaf']
say_hi1(anggota_boyband)
'''' latihan fungsi '''

import os


# program menghitung luas dan keliling persegi

def header():
    os.system('cls')
    print('PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI')
    print('_' * 40)


def input_user():
    ''''fungsi input user'''
    # mengambil input user
    lebar = int(input('Masukkan lebar persegi: '))
    panjang = int(input('Masukkan panjang persegi: '))

    return lebar, panjang


def hitung_luas(lebar, panjang):
    ''''fungsi hitung luas'''
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    ''''fungsi hitung keliling'''
    return 2*(lebar + panjang)

def display(message,value):
    ''''fungsi display'''
    print(f'hasil perhitungan {message} : {value}')

# program utamnya
while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display('luas', LUAS)
    display('keliling', KELILING)

    isContinue = input('\nApakah ingin melanjutkan? (y/n) : ')
    if isContinue == 'n':
        break
print('program selesai')


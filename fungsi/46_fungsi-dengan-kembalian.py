# fungsi dengan kembalian

# template fungsi dengan kembalain
# def nama_fungsi(argument):
#     badan fungsi
#     return outpuy

# contoh fungsi dengan kembalian
# fungsi kuadrat

def kuadrat(input_angka):
    ''' Fungsi Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat
y = kuadrat(6)
print(y)

print(kuadrat(6))

# fungsi tambah

def fungsi_tambah(angka_1, angka_2):
    ''' fungsi return dengan multi input'''
    return angka_1 * angka_2
a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1, angka2):
    '''fungsi return dengan multi input'''
    tambah = angka_1 + angka2
    kurang = angka_1 - angka2
    kali = angka_1 * angka2
    bagi = angka_1 / angka2

    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(10,8)
print(f'tambah\t:{k}')
print(f'kurang\t:{l}')
print(f'kali\t:{m}')
print(f'bagi\t:{n}')
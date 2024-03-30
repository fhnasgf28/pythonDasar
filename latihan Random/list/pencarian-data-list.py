print('=======================Program Pencarian Data List======================')

n = int(input('Input Jumlah Element List\t:'))
print()

print('input',n, 'angka (dipisahkan dengan enter)')

# simpan setiap angka yang diinputkan kedalam list
x = []
for i in range(n):
    print('Angka ke-', i + 1, ':', sep='', end='')
    x.append(int(input()))
print()

num = int(input('Input angka yang akan dicari\t:'))

# proses pencarian element list
for i in range(n):
    if x[i]==num:
        print('Angka ditemukan pada urutan ke', i + 1)
        break
if 1 != n:
    pass
else:
    print('Angka Tidak ditemukan')

nilai_tertinggi = x[0]
for i in range(1, n):
    if x[i] > nilai_tertinggi:
        nilai_tertinggi = x[i]

print("Nilai Tertinggi adalah", nilai_tertinggi)
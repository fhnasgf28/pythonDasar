print('## Program Python Penjumlahan List/arry')
print('====================================')
print()

n = int(input('Input Jumlah Element List\t'))
print()

print('Input', n, 'angka(dipisahkan dengan enter)\t')

#simpan setiap angka yang diinput ke dalalm list

x = []
for i in range(n):
    print('angka ke',i+1, ':',sep=' ', end='')
    x.append(int(input()))

    print()

# cari total semua element list
total = 0
for i in range(n):
    total = total+x[i]

print('Total Penjumlahan dari', n, 'angka tersebut adalah\t:',total)
# contoh kode program operator bitwise dalam bahasa Py

x = 10 
y = 12 

print('x berisi angka',x,'desimal atau',bin(x),'biner')
print('x berisi angka',y,'desimal atau',bin(y),'biner')

print('\n')

print('x dan y :', x & y)
print('x dan y :', x | y)
print('x dan y :', x ^ y)

# penggunaan operator bitwise
a = 60
b = 13
c = 0

c = a & b
print("Nilai c = ", c)

c = a | b
print("Nilai c = ", c)

c = a ^ b
print("Nilai c = ", c)
# menyelesaikan persamaan quadrat ax**2 + bx + c = 0

# mengimpor modul Cmath
import cmath

# menginput angka
a = int(input("Tulis a\t:"))
b = int(input("Tulis b\t:"))
c = int(input("Tulis C\t:"))

#menghitung diskriminan
d = (b**2) - (4*a*c)

#menghitung x1 dan x2
x1 = (-b-cmath.sqrt(d)/(2*a))
x2 = (-b+cmath.sqrt(d)/(2*a))

# menampilkan hasil x1 dan x2
print('Hasil persamaan quadrat adalah {0} dan {1}'.format(x1,x2))
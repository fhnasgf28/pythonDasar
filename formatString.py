# string

nama = "ucup"
format_str = f"Hallo {nama}"
print(format_str)

# boolean 
boolean = False
format_str = f"Boolan = {boolean}"
print(format_str)

# angka
angka = 20004.4
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15 
format_str = f"angka : {angka}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 200000
format_str = f"jutaan : {angka:,}"
print(format_str)

# bilangan desimal 
angka = 20005.33453
format_str = f"desimal: {angka:.2f}"
print(format_str) 

# menampilkan leading zero

angka = 20005.33453
format_str = f"desimal: {angka:02.3f}"
print(format_str) 

# menampilkan tanda + -
angka_minus = -10
angka_plus = +10.324
forma_minus = f"minus: {angka_minus:-d}"
forma_plus = f"plus: {angka_plus:+.2f}"

print(forma_minus)

print(forma_plus)

# memformat persen

persentase = 0.34234
format_persen = f"Persen: {persentase:.3%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah =5 

format_string = f"harga total = Rp. {harga * jumlah:,}"
print(format_string)
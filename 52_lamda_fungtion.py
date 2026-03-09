# lambda fungtion

def f_kuadrat(angka):
    return angka ** 2


print(f"Hasil fungsi kuadrat = {f_kuadrat(5)}")

# kita coba dengan lambda
# output = lambda argument:expression

kuadrat = lambda angka: angka ** 2
print(f"Hasil lambda kuadrat = {kuadrat(4)}")

pangkat = lambda num, pow: num ** pow
print(f"Hasil lamda pangkat = {pangkat(4, 2)}")

# kagunaan apa bang

# sorting untuk list biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted List = {data_list}")


# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sort pakai lamda
data_list = ["otong", "ucup", "Dudung"]
data_list.sort(key=lambda nama: len(nama))
print(f"Sorted list by lambda = {data_list}")

# filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 5]


def kurang_dari_lima(angka):
    return angka < 5


data_angka_new = list(filter(kurang_dari_lima, data_angka))
data_angka_new = list(filter(lambda x: x < 7, data_angka))
print(data_angka_new)

# kasus genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: x % 2 != 0, data_angka))
print(data_ganjil)

# anonymous fungtion
# currying <- Haskel Curry

def pangkat(angka, n):
    hasil = angka ** n
    return hasil
data_hasil = pangkat(5, 3)
print(f"Fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(10)}")

pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")

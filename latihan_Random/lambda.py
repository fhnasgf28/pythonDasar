
# fungsi untuk menghitung nilai maksimum dari dua bilangan
def max_value(a, b, compare_fn):
    return a if compare_fn(a, b) else b

# lambda untuk membandingkan dua bilangan berdasarkan nilai absolutenya
compare_abs = lambda x, y: abs(x) > abs(y)

# menemukan nilai maksimum dari 2 dan -3
print(max_value(2, -3, compare_abs))

# filter map dengan lambda

nama = ["Andi", "Budi", "Cici", "Deni"]

# memfilter nama yang dimulai dengan huruf "A"

nama_a = list(filter(lambda nama: nama[0] == "A", nama))

# mengubah nama menjadi kapital
nama_kapital = list(map(lambda nama: nama.upper(), nama))

print(nama_a)
print(nama_kapital)
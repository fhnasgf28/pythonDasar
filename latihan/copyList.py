# Teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah dari member a
# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan menggunakan copy
print("menduplikat list dengan menggunakan copy")

c = a.copy() #full duplicat / data baru
print(f"c = {c}")

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# kita ubah data 0
c[0] = "Farhan Assegaf"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# kita ubah data 1
print("="*10,"ubah data 1","="*10)
a[1] = "Assegaf"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
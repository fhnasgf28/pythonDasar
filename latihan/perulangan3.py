#1 menggunakan for
sisi =10
#dummy variabel
print("awal For")
count = 1 
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir For")

# menggunakan while
print("awal while")
count = 2
while True:
    print("*"*count)
    count += 2
    if count > sisi:
        break
    else:
        # akan kembali ke atas jika ganjil
        count += 2
        continue
    if count > sisi:
        break

print("akhir while")

# 4 hanya ganjil saja
print("awal while")
count = 6 
spasi = int(sisi/2)

while True:
    if (count %2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    if count > sisi:
        break

print("akhir while")
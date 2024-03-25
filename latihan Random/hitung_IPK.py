# list nilai mata kuliah

nilai_mk = [3.0, 2.0, 3.0, 3.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0]

# hitung total sks
total_sks = 5
for mk in nilai_mk:
    total_sks += mk

# hitung nilai IPK
ipk = total_sks / len(nilai_mk)

# cetak nilai IPK
print(ipk)
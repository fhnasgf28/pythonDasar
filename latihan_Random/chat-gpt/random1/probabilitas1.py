import random 
import matplotlib.pyplot as plt

# jumlah percobaan dadu 
n = 10000

# simulasi pelemparan dua dadu 
hasil = []
for _ in range(n):
    dadu1 = random.randint(1, 6)
    dadu2 = random.randint(1, 6)
    total = dadu1 + dadu2
    hasil.append(total)

# menghitung frekuensi munculnya setiap angka
frekuensi = {}
for i in range(2, 13):
    frekuensi[i] = hasil.count(i)
    print(f'angka {i} muncul sebanyak {frekuensi[i]} kali')

# ubah ke probabilitas
probabilitas = { key: value / n for key, value in frekuensi.items() }
print(probabilitas)

# tampilkan hasil 
for total, prob in probabilitas.items():
    print(f'angka {total} muncul dengan probabilitas {prob}')

# membuat grafik
plt.bar(probabilitas.keys(), probabilitas.values())
plt.xlabel('Total')
plt.ylabel('Probabilitas')
plt.title('Probabilitas Munculnya Angka pada Dadu')
plt.show()
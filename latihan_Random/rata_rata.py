# menginputkan jumlah bilangan
jumlah_bilangan = int(input("Masukkan Jumlah bilangan\t:"))

# menampung daftar bilangan
bilangan = []

# mengumpulkan bilangan dari user
for i in range(jumlah_bilangan):
    bilangan.append(int(input("Masukan Bilangan ke-{}".format((i + 1)))))
# menghitung total bilangan
total =sum(bilangan)

# menghitung nilai rata-rata
rata_rata = total / jumlah_bilangan

# menampilkan hasil
print("Nilai rata-rata dari {} bilangan adalah: {}".format(jumlah_bilangan, rata_rata))
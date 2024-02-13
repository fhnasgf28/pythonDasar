# jawab = 'ya'
# hitung = 0

# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input("ulangi lagi tidak ? ")
# print(f"Total Perulangan: {hitung}")

# break

# menginputkan jumlah angka 
jumlah_angka = int(input("Masukan Jumlah Agka \t:"))

# Menginisialisasi variabel total dan rata-rata
total = 0
rata_total = 0

# melakukan perulangan untuk setiap angka
for i in range(jumlah_angka):
    for j in range(4):
        try:
            angka = int(input("Masukan Angka ke-\t:" + str(i + 1) + ": "))
            break
        except ValueError:
            print("Masukan angka saja")
            if j == 4:
                print("Batas Percobaan input terlampaui")
                exit()
    # menambahkan nilai angka ke total
    total += angka
    # menghitung rata-rata
    rata_rata = total / jumlah_angka

# menampilkan hasil total dan rata-rata
print("Total:", total)
print("Rata-rata:", rata_rata)




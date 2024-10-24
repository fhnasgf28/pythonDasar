
# membuat list untuk menyimpan nama dan umur
names = []
ages = []

while True:
    name = input("Masukan Nama: ")
    if name.lower() == "selesai":
        break
    age = int(input("Masukan Umur: "))

    names.append(name)
    ages.append(age)

    # mencetak semua nama dan umur
    print("Data Mahasiswa:")
    for i in range(len(names)):
        print(f"Nama: {names[i]}, Umur: {ages[i]}")
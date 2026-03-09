def urutkan_angka(angka):
    return sorted(angka)

# contoh penggunaan
input_angka = input("Masukkan daftar angka (pisahkan dengan koma): ")
daftar_angka = list(map(int,filter(None, input_angka.split(","))))

urutkan = urutkan_angka(daftar_angka)
print("Daftar angka setelah diurutkan:", urutkan)
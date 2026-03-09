# buat dictionary ksosong
import json

# buka file JSON dalam mode append
with open("data_penggun.json", "a") as file:

    data_pengguna = {}
# looping untuk memasukan data pengguna
    while True:
        nama = input("Masukkan Nama : ")
        while not nama.isalpha():
            nama = input("Nma harus berupa huruf, masukan kembali")
        alamat = input("Masukkan Alamat : ")
        while not alamat.isalpha():
            alamat = input("Alamat harus berupa huruf, masukan kembali")

        # simpan data kedalam dictionary
        data_pengguna[nama] = alamat

        # tanyakan apakah pengguna ingin memasukan data lagi
        lagi = input("Apakah ingin memasukan data lagi? (y/n) : ")
        if lagi.lower() == "n":
            break
        json.dump(data_pengguna, file)

    # cetak isi dictionary
for nama, alamat in data_pengguna.items():
    print(f"Nama: {nama}")
    print(f"Alamat: {alamat}")
    print()

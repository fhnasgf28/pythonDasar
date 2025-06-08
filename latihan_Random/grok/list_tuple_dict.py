import json

# list untuk menyimpan semua data mahasiswa
daftar_mahasiswa = []
def tambah_mahasiswa():
    # input data mahasiswa
    nama = input("Masukan Nama: ")
    nim = input("Masukkan Nim: ")

    # tuple untk menyimpan mata kuliah
    mata_kuliah = ("Matematika", "Fisika", "Kimia", "Biologi")

    # dict untuk menyimpan data nilai
    nilai = {}
    for matkul in mata_kuliah:
        skor = int(input(f"Masukan Nilai {matkul}: "))
        nilai[matkul] = skor

    # dict untuk menyimpan data mahasiswa
    data_mahasiswa = {
        "nama": nama,
        "nim": nim,
        "nilai": nilai,
        "mata_kuliah": mata_kuliah
    }
#     tambah data mahasiswa ke daftar mahasiswa
    daftar_mahasiswa.append(data_mahasiswa)
    print("Data Mahasiswa Berhasil Ditambahkan")

def simpan_ke_json():
    data_json = json.dumps(daftar_mahasiswa, indent=4)
    print("data dalam format json", data_json)

    with open("daftar_mahasiswa.json", "w") as f:
        json.dump(daftar_mahasiswa, f, indent=4)
    print("Data Berhasil Disimpan")

# menjalankan program
while True:
    print("1. Tambah Mahasiswa")
    print("2. Simpan ke JSON")
    print("3. Keluar")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan == "2":
        simpan_ke_json()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid")





import json

# Daftar buku (dalam bentuk dictionary)

books = [
    {"judul": "Python untuk Pemula", "penulis": "Andi", "tahun": 2020, "genre": "Programming"},
    {"judul": "Data Science dengan Python", "penulis": "Budi", "tahun": 2021, "genre": "Data Science"},
    {"judul": "Belajar Machine Learning", "penulis": "Citra", "tahun": 2022, "genre": "Machine Learning"},
    {"judul": "Deep Learning", "penulis": "Andi", "tahun": 2023, "genre": "Machine Learning"}
]

# fungsi untuk mencari buku berdasarkan judul
def cari_buku_judul(judul):
    hasil_pencarian = []
    for buku in books:
        if judul.lower() in buku["judul"].lower():
            hasil_pencarian.append(buku)
        return hasil_pencarian

# fungsi untuk menyimpan hasil pencarian dalam format JSON
def simpan_ke_json(data, nama_file):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

# contoh penggunaan
judul_yang_dicari = "python"
hasil = cari_buku_judul(judul_yang_dicari)

# simpan hasil dalam file JSON
simpan_ke_json(hasil, "hasil_pencarian.json")
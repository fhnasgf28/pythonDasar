#!/usr/bin/env python3

# 1. Dictionary dengan berbagai tipe data
siswa = {
    'nama': 'Budi Santoso',
    'umur': 17,
    'nilai': [85, 90, 88],
    'aktif': True,
    'hobi': ('Membaca', 'Menulis'),
    'alamat': {
        'jalan': 'Jl. Merdeka No. 123',
        'kota': 'Jakarta',
        'kode_pos': '12345'
    }
}

# 2. Operasi dasar dictionary
print("=== Operasi Dasar Dictionary ===")
# Menambah item baru
siswa['email'] = 'budi@example.com'

# Mengubah nilai
siswa['umur'] = 18

# Menghapus item
if 'hobi' in siswa:
    del siswa['hobi']

# Mengakses nilai dengan get() (lebih aman)
print(f"Nama: {siswa.get('nama', 'Tidak ada')}")
print(f"Jurusan: {siswa.get('jurusan', 'Belum ada jurusan')}")

# 3. Dictionary Comprehension
print("\n=== Dictionary Comprehension ===")
angka = range(1, 6)
kuadrat = {n: n**2 for n in angka}
print("Kuadrat:", kuadrat)

# 4. Nested Dictionary (Dictionary bersarang)
print("\n=== Nested Dictionary ===")
perpustakaan = {
    'buku_1': {
        'judul': 'Python Programming',
        'penulis': 'John Doe',
        'tahun': 2022,
        'tersedia': True
    },
    'buku_2': {
        'judul': 'Data Science Basics',
        'penulis': 'Jane Smith',
        'tahun': 2021,
        'tersedia': False
    }
}

# Mengakses nested dictionary
for kode_buku, info in perpustakaan.items():
    print(f"\nInformasi {kode_buku}:")
    for key, value in info.items():
        print(f"{key}: {value}")

# 5. Dictionary Methods
print("\n=== Dictionary Methods ===")
menu_makanan = {
    'nasi_goreng': 15000,
    'mie_goreng': 12000,
    'sate': 20000
}

# Mendapatkan semua keys
print("Menu yang tersedia:", list(menu_makanan.keys()))

# Mendapatkan semua values
print("Daftar harga:", list(menu_makanan.values()))

# Mendapatkan pasangan key-value
print("Menu dan Harga:", list(menu_makanan.items()))

# 6. Menggabungkan Dictionary
print("\n=== Menggabungkan Dictionary ===")
menu_minuman = {
    'es_teh': 5000,
    'es_jeruk': 6000
}

# Cara 1: update()
menu_lengkap = menu_makanan.copy()
menu_lengkap.update(menu_minuman)
print("Menu Lengkap:", menu_lengkap)

# Cara 2: menggunakan operator |= (Python 3.9+)
menu_makanan |= menu_minuman
print("Menu Lengkap (cara 2):", menu_makanan)

# 7. Dictionary dengan fromkeys()
print("\n=== Dictionary dengan fromkeys() ===")
nama_buah = ['apel', 'jeruk', 'mangga']
harga_default = 0
inventory_buah = dict.fromkeys(nama_buah, harga_default)
print("Inventory Buah:", inventory_buah)

# 8. Contoh praktis: Menghitung frekuensi kata
print("\n=== Menghitung Frekuensi Kata ===")
teks = "saya suka python karena python adalah bahasa pemrograman yang python banget"
kata_kata = teks.split()
frekuensi = {}

for kata in kata_kata:
    frekuensi[kata] = frekuensi.get(kata, 0) + 1

print("Frekuensi kata:", frekuensi) 
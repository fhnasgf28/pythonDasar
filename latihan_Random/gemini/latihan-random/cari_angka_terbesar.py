# def cari_angka_terbesar(angka):
#     # mencari angka terbesar dari list
#     if not angka:
#         return None
#     terbesar = angka[0]
#     for number in angka:
#         if number > terbesar:
#             terbesar = number
#     return terbesar

# def balik_list(daftar):
#     # membalikan urutan element dalam list
#     return daftar[::-1]

# angka = [3, 5, 7, 2, 8, 6]
# print("Angka terbesar:", cari_angka_terbesar(angka))
# print("List dibalik:", balik_list(angka))
# # Output:

def kelompokkan_berdasarkan_kategori(daftar_item, kunci_kategori):
    kelompok = {}
    for item in daftar_item:
        kategori = item.get(kunci_kategori)
        if kategori not in kelompok:
            kelompok[kategori] = []
        kelompok[kategori].append(item)
    return kelompok
# Contoh penggunaan
daftar_item = [
    {'nama': 'Buku', 'kategori': 'Alat Tulis'},
    {'nama': 'Pensil', 'kategori': 'Alat Tulis'},
    {'nama': 'Penghapus', 'kategori': 'Alat Tulis'},
    {'nama': 'Baju', 'kategori': 'Pakaian'},
    {'nama': 'Celana', 'kategori': 'Pakaian'}
]

kunci_kategori = 'kategori'
kelompok = kelompokkan_berdasarkan_kategori(daftar_item, kunci_kategori)
print(kelompok)
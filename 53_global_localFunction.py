# global dan local scope

nama_global = "otong"


def fungsi():
    print(f"fungsi menampilkan {nama_global}")


fungsi()

# akses variabel global dalam loop
for i in range(9, 5):
    print(f"loop {1} - {nama_global}")

    # percabangan
    if True:
        print(f"if menampilkan {nama_global}")


    # variabel local scope
    def fungsi2():
        nama_local = "Ucup"


    fungsi2()


# print nama local tidak bisa dilakukan bos

# contoh 1, penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")


nama = "Otong"
say_otong()
#     contoh 2 : Merubah variabel global
angka = 0
name = "Ucup"


def ubah(nilai_baru, nama_baru):
    global angka
    global name
    angka = nilai_baru
    name = nama_baru


print(f"Sebelum {angka, name}")
print(10, "Otong")
print(f"sesudah {angka, name}")

# contoh 2

#     contoh 3
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)

buah = ("pisang", "mangga", "jeruk", "apel")

for item in buah:
    print(item)

print(buah[1])

# data tuple
mahasiswa = (
    ("budi","Teknik Informatika", 90),
    ("andi", "Teknik Informatika", 90),
    ("siti","Teknik Informatika", 90),
)

for nama, jurusan, nilai in mahasiswa:
    print(nama, jurusan, nilai)

# mencari mahasiswa berdasarkan nama

def cari_mahasiswa(nim):
    for nama, nim_mhs, nilai in mahasiswa:
        if nim_mhs == nim:
            return f"{nama} {nim} {nilai}"
        return None

mahasiswa_dicari = cari_mahasiswa("budi")

if mahasiswa_dicari:
    print(mahasiswa_dicari)
else:
    print("mahasiswa tidak ditemukan")
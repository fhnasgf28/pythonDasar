import pandas as pd

siswa = [
    {"nia": "2024001", "nama": "Andi", "kelas": "10A"},
    {"nia": "2024002", "nama": "Budi", "kelas": "10B"},
    {"nia": "2024001", "nama": "Citra", "kelas": "10A"},
    {"nia": "2024003", "nama": "Dewi", "kelas": "11A"},
    {"nia": "2024002", "nama": "Eko", "kelas": "10B"},
    {"nia": "2024004", "nama": "Farah", "kelas": "11B"},
]

# mengelompokkan siswa berdasarkan NIA
kelompok_siswa = {}
for data in siswa:
    nia = data["nia"]
    if nia not in kelompok_siswa:
        kelompok_siswa[nia] = []
    kelompok_siswa[nia].append(data)


# menampilkan hasil pengelompokn
print("Pengelompokkan siswa berdasarkan NIA:")
for nia, daftar_siswa in kelompok_siswa.items():
    print(f"NIA: {nia}")
    for s in daftar_siswa:
        print(f"- Nama: {s['nama']}, Kelas: {s['kelas']}")
    print()

# menampilkan data dalam tabel dengan pandas
df = pd.DataFrame(siswa)
print("dalam dalam bentuk tabel:")
print(df.groupby("nia").agg({"nama": "first", "kelas": "first"}))
print(df.groupby("nia").apply(lambda x: x[["nama", "kelas"]].head(1)))
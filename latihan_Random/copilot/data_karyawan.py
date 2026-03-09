karyawan = [
    {"id": 1, "nama": "Ahmad", "posisi": "Manager", "gaji": 10000000, "tahun_mulai": 2015},
    {"id": 2, "nama": "Siti", "posisi": "Developer", "gaji": 8000000, "tahun_mulai": 2018},
    {"id": 3, "nama": "Budi", "posisi": "Designer", "gaji": 7000000, "tahun_mulai": 2020},
    {"id": 4, "nama": "Mira", "posisi": "Developer", "gaji": 8500000, "tahun_mulai": 2017},
]

def tampilkan_karyawan(data):
    print("Daftar Karyawan:")
    for karyawan in data:
        print(f"ID: {karyawan['id']}")
        print(f"Nama: {karyawan['nama']}")
        print(f"Posisi: {karyawan['posisi']}")
        print(f"Gaji: {karyawan['gaji']}")
        print(f"Tahun Mulai: {karyawan['tahun_mulai']}")

# menambahkan karyawan baru
def tambah_karyawan(data):
    id_karyawan = int(input("Masukkan ID karyawan: "))
    nama = input("Masukkan nama karyawan: ")
    posisi = input("Masukkan posisi karyawan: ")
    gaji = int(input("Masukkan gaji karyawan: "))
    tahun_mulai = int(input("Masukkan tahun mulai bekerja: "))

    data.append({
        "id": id_karyawan,
        "nama": nama,
        "posisi": posisi,
        "gaji": gaji,
        "tahun_mulai": tahun_mulai
    })
    print("Karyawan berhasil ditambahkan.")

def rata_gaji(data):
    total_gaji = sum(karyawan["gaji"] for karyawan in data)
    rata_rata = total_gaji / len(data)
    print(f"Rata-rata gaji karyawan: {rata_rata}")
    return rata_rata

def cari_karyawan(data, id_karyawan):
    for karyawan in data:
        if karyawan["id"] == id_karyawan:
            print(f"Karyawan dengan ID {id_karyawan} ditemukan:")
            print(f"Nama: {karyawan['nama']}")
            print(f"Posisi: {karyawan['posisi']}")
            print(f"Gaji: {karyawan['gaji']}")
            print(f"Tahun Mulai: {karyawan['tahun_mulai']}")
            return
    print(f"Karyawan dengan ID {id_karyawan} tidak ditemukan.")

# menentukan karyawan senior
def karyawan_senior(data):
    senior = min(data, key=lambda karyawan: karyawan["tahun_mulai"])
    print(f"Karyawan senior: {senior['nama']} ({senior['tahun_mulai']})")


def main():
    while True:
        print("\nManajemen Data Karyawan")
        print("1. Tampilkan daftar karyawan")
        print("2. Tambah karyawan baru")
        print("3. Hitung rata-rata gaji")
        print("4. Cari karyawan berdasarkan ID")
        print("5. Tampilkan karyawan senior")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tampilkan_karyawan(karyawan)
        elif pilihan == "2":
            tambah_karyawan(karyawan)
        elif pilihan == "3":
            rata_gaji(karyawan)
        elif pilihan == "4":
            id_karyawan = int(input("Masukkan ID Karyawan: "))
            cari_karyawan(karyawan, id_karyawan)
        elif pilihan == "5":
            karyawan_senior(karyawan)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()

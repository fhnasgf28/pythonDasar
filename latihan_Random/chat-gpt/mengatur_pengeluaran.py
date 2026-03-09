import json
import os

file_pengeluaran = "pengeluaran.json"

def load_data():
    if os.path.exists(file_pengeluaran):
        with open(file_pengeluaran, 'r') as file:
            return json.load(file)

    return []

def save_data():
    with open(file_pengeluaran, 'w') as file:
        json.dump(pengeluaran, file, indent=4)

pengeluaran = load_data()

def tambah_pengeluaran():
    tanggal = input("Masukan tanggal pengeluaran (dd-mm-yyyy): ")
    kategori = input("Masukan kategori pengeluaran: ")
    nominal = int(input("Masukan nominal pengeluaran: "))
    pengeluaran.append({'tanggal': tanggal, 'kategori': kategori, 'nominal': nominal})
    print("Pengeluaran berhasil ditambahkan")
    print(f"ini adalah pengeluran{pengeluaran}")

def lihat_semua():
    print("Daftar pengeluaran:")
    for idx, p in enumerate(pengeluaran, 1):
        print(f"{idx}. {p['tanggal']} - {p['kategori']} - {p['nominal']}")
        save_data()
    print()

def total_per_hari():
    tanggal = input("Masukan tanggal (dd-mm-yyyy): yang akan di cek")
    total = sum(p['nominal'] for p in pengeluaran if p['tanggal'] == tanggal)
    print(f"Total pengeluaran pada tanggal {tanggal} adalah: {total}")

def filter_kategori():
    kategori = input("Masukan kategori yang akan di filter: ")
    print(f"Pengeluaran dengan kategori {kategori}:")
    for p in pengeluaran:
        if p['kategori'].lower() == kategori.lower():
            print(f"{p['tanggal']} - {p['kategori']} - {p['nominal']}")
            print()

def main():
    while True:
        print("--- Aplikasi Manajemen Pengeluaran Harian ---")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Semua Pengeluaran")
        print("3. Total Pengeluaran Per Hari")
        print("4. Filter Pengeluaran Berdasarkan Kategori")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_pengeluaran()
        elif pilihan == "2":
            lihat_semua()
        elif pilihan == "3":
            total_per_hari()
        elif pilihan == "4":
            filter_kategori()
        elif pilihan == "5":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

if __name__ == "__main__":
    main()
import json
import os

file_karyawan = "karyawan.json"

def load_data():
    if os.path.exists(file_karyawan):
        with open(file_karyawan, 'r') as file:
            return json.load(file)
    return[]

def save_data(data):
    with open(file_karyawan, 'w') as file:
        json.dump(data, file, indent=4)

karyawan = load_data()

def tambah_karyawan():
    id_karyawan = input("Masukkan ID karyawan: ")
    nama = input("Masukkan Nama: ")
    jabatan = input("Masukkan Jabatan: ")
    gaji = int(input("Masukkan Gaji: "))

    data_baru = {
        "id": id_karyawan,
        "nama": nama,
        "jabatan": jabatan,
        "gaji": gaji
    }

    karyawan.append(data_baru)
    save_data(karyawan)
    print("Karyawan berhasil ditambahkan.")

def lihat_karyawan():
    if not karyawan:
        print("Belum ada data karyawan.")
        return
    for k in karyawan:
        print(f"ID: {k['id']} | Nama: {k['nama']} | Jabatan: {k['jabatan']} | Gaji: {k['gaji']}")
    print()

def perbaharui_karyawan():
    id_karyawan = input("Masukkan ID karyawan: ")
    for k in karyawan:
        if k["id"] == id_karyawan:
            print("\npilih data yang ingin diperbaharui")
            print("1. jabatan")
            print("2. gaji")
            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == "1":
                jabatan_baru = input("Masukkan Jabatan Baru: ")
                k["jabatan"] = jabatan_baru
            elif pilihan == "2":
                gaji_baru = int(input("Masukkan Gaji Baru: "))
                k["gaji"] = gaji_baru
            save_data(karyawan)
            print("Data karyawan berhasil diperbaharui.")
            return
    print("ID karyawan tidak ditemukan.")

def hapus_karyawan():
    id_karyawan = input("Masukkan ID karyawan yang ingin dihapus: ")
    global karyawan
    karyawan_baru = [k for k in karyawan if k["id"] != id_karyawan]

    if len(karyawan) == len(karyawan_baru):
        print("ID karyawan tidak ditemukan.")
    else:
        karyawan = karyawan_baru
        save_data(karyawan)
        print("Karyawan berhasil dihapus.")

def main():
    while True:
        print("🏢 Sistem Manajemen Karyawan 🏢")
        print("1. Tambah Karyawan")
        print("2. Lihat Daftar Karyawan")
        print("3. Perbarui Data Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            lihat_karyawan()
        elif pilihan == "3":
            perbaharui_karyawan()
        elif pilihan == "4":
            hapus_karyawan()
        elif pilihan == "5":
            print("🚀 Terima kasih! Sampai jumpa.")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.\n")

if __name__ == "__main__":
    main()

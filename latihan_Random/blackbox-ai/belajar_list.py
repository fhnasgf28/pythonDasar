def tampilkan_menu():
    print("/n===== Aplikasi Manajement Data siswa ===")
    print("1. Tambah Siswa")
    print("2. Tampilkan Daftar Siswa")
    print("2. Hapus Siswa")
    print("4. Keluar")

def tambah_siswa(siswa_list):
    nama = input("Masukkan nama siswa: ")
    umur = input("Masukkan umur siswa: ")
    siswa_list.append({"nama": nama, "umur": umur})
    print(f"Siswa {nama} berhasil ditambahkan.")

def tampilkan_daftar_siswa(siswa_list):
    if not siswa_list:
        print("Daftar siswa kosong.")
    else:
        print("\nDaftar siswa:")
        for index, siswa in enumerate(siswa_list, start=1):
            print(f"{index}. Nama: {siswa['nama']}, Umur: {siswa['umur']}")


def hapus_siswa(siswa_list):
    name = input("Masukkan nama siswa yang ingin dihapus: ")
    for siswa in siswa_list:
        if siswa["nama"].lower() == name.lower():
            siswa_list.remove(siswa)
            print(f"Siswa {name} berhasil dihapus.")
            return
    print(f"Siswa {name} tidak ditemukan.")


def main():
    siswa_list = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            tambah_siswa(siswa_list)
        elif pilihan == '2':
            tampilkan_daftar_siswa(siswa_list)
        elif pilihan == '3':
            hapus_siswa(siswa_list)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi manajemen data siswa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan aplikasi
if __name__ == "__main__":
    main()

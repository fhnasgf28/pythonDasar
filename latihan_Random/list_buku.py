
import json
import os
def tampilkan_menu():
    # aplikasi manajemen buku
    print("\n=== Aplikasi Manajemen Buku ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Daftar Buku")
    print("3. Hapus Buku")
    print("4. Keluar")

def tambah_buku(buku_list):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    buku_list.append({"judul": judul, "penulis": penulis})

def tampilkan_daftar_buku(buku_list):
    print("\nDaftar Buku:")
    if not buku_list:
        print('Belum ada buku')
    else:
        print("\nDaftar Buku:")
        for index, buku in enumerate(buku_list, start=1):
            print(f"{index}. {buku['judul']} - {buku['penulis']}")
        simpan_daftar_buku(buku_list)
    print("\n")

def cari_buku(buku_list):
    judul = input("Masukkan judul buku yang ingin dicari: ")
    for buku in buku_list:
        if buku['judul'].lower() == judul.lower():
            print(f"Buku ditemukan: {buku['judul']} - {buku['penulis']}")
            return
    print(f"Buku {judul} tidak ditemukan.")

def simpan_daftar_buku(buku_list):
    data = {"buku_list": buku_list}
    with open('daftar_buku.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Daftar buku berhasil disimpan.")

def hapus_buku(buku_list):
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    for buku in buku_list:
        if buku['judul'].lower() == judul.lower():
            buku_list.remove(buku)
            print(f"Buku {judul} telah dihapus.")
            return
    print(f"Buku {judul} tidak ditemukan.")

def main():
    buku_list = []
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            tambah_buku(buku_list)
        elif pilihan == "2":
            tampilkan_daftar_buku(buku_list)
        elif pilihan == "3":
            cari_buku(buku_list)
        elif pilihan == "4":
            hapus_buku(buku_list)
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
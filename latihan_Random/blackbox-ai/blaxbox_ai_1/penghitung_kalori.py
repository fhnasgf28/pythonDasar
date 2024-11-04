def tampilkan_menu():
    print("\n=== Aplikasi Penghitung Kalori ===")
    print("1. Tambah Makanan")
    print("2. Hapus Makanan")
    print("3. Tampilkan Total Kalori")
    print("4. Keluar")


def tambah_makanan(kalori_dict):
    makanan = input("Masukkan nama makanan: ")
    kalori = float(input("Masukkan jumlah kalori: "))
    kalori_dict[makanan] = kalori
    print(f"{makanan} telah ditambahkan dengan {kalori} kalori.")


def hapus_makanan(kalori_dict):
    makanan = input("Masukkan nama makanan yang ingin dihapus: ")
    if makanan in kalori_dict:
        del kalori_dict[makanan]
        print(f"{makanan} telah dihapus.")
    else:
        print(f"{makanan} tidak ditemukan dalam daftar.")


def tampilkan_total_kalori(kalori_dict):
    if not kalori_dict:
        print("Tidak ada makanan yang telah Anda konsumsi.")
    else:
        total_kalori = sum(kalori_dict.values())
        print(f"Total kalori yang telah Anda konsumsi: {total_kalori} kalori")


def main():
    kalori_dict = {}

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            tambah_makanan(kalori_dict)
        elif pilihan == '2':
            hapus_makanan(kalori_dict)
        elif pilihan == '3':
            tampilkan_total_kalori(kalori_dict)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi penghitung kalori!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan aplikasi
if __name__ == "__main__":
    main()
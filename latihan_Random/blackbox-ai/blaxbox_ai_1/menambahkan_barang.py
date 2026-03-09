def display_menu():
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Hapus Barang")
    print("4. Keluar")


def add_item(items):
    item = input("Masukkan nama barang yang ingin ditambahkan: ")
    items.append(item)
    print("Barang berhasil ditambahkan.", item)


def view_items(items):
    if items:
        print("Daftar Barang:")
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")
    else:
        print("Daftar barang kosong.")

def remove_item(items):
    item = input("Masukkan nama barang yang ingin dihapus: ")
    if item in items:
        items.remove(item)
        print("Barang berhasil dihapus.", item)
    else:
        print("Barang tidak ditemukan.")


def main():
    items = []
    while True:
        display_menu()
        choice = input("Pilih Opsi (1/2/3/4):")
        if choice == '1':
            add_item(items)
        elif choice == '2':
            view_items(items)
        elif choice == '3':
            remove_item(items)
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
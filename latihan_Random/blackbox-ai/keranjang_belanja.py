import json
import os

# Nama file untuk menyimpan keranjang belanja
FILENAME = 'keranjang.json'

def load_cart():
    # membaca keranjang dari file JSON
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_cart(cart):
    '''Menyimpan data keranjang ke file JSON'''
    with open(FILENAME, 'w') as file:
        json.dump(cart, file, indent=4)

def add_item_to_cart(cart, item):
    '''Menambahkan item ke keranjang dan menyimpan ke file'''
    cart.append(item)
    save_cart(cart)
    print(f"item '{item}' telah ditambahkan ke keranjang")

def display_cart(cart):
    '''Menampilkan isi keranjang'''
    if cart:
        print("Isi Keranjang: ")
        for idx, item in enumerate(cart, start=1):
            print(f"{idx}. {item}")
    else:
        print("Keranjang Kosong.")

def main():
    cart = load_cart()
    while True:
        print("\nMenu:")
        print("1. Tambah barang ke keranjang")
        print("2. Tampilkan Keranjang")
        print("3. Keluar")
        choice = input("Pilih Opsi (1/2/3):")

        if choice == '1':
            item = input("Masukkan nama barang ;")
            add_item_to_cart(cart, item)
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
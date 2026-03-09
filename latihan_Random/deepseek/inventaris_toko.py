def tampilkan_inventaris(inventaris):
    print("Daftar Inventaris Toko:")
    for idx, item in enumerate(inventaris, start=1):
        print(f"{idx}. {item['nama']} - Stok: {item['stok']} - Harga: {item['harga']}")

# def manajement stok
def tambah_item(inventaris, nama, stok, harga):
    item_baru = {"nama": nama, "stok": stok, "harga": harga}
    inventaris.append(item_baru)
    print(f"Item '{nama}' berhasil ditambahkan ke inventaris.")

def update_stok(inventaris,nama, jumlah):
    for item in inventaris:
        if item["nama"] == nama:
            item["stok"] += jumlah
            print(f"Stok '{nama}' berhasil diperbarui menjadi {item['stok']}.")
            return

    print(f"Item '{nama}' tidak ditemukan dalam inventaris.")

# analisis data
def cari_termahal(inventaris):
    if not inventaris:
        return None
    return max(inventaris, key=lambda item: item["harga"])

def total_nilai(inventaris):
    return sum(item["harga"] * item["stok"] for item in inventaris)

# main program
def main():
    inventaris = [
        {"nama": "Laptop", "stok": 5, "harga": 100000},
        {"nama": "Smartphone", "stok": 10, "harga": 50000},
        {"nama": "Kamera", "stok": 3, "harga": 200000}
    ]

    while True:
        print("\nMenu:")
        print("1. Tampilkan Inventaris")
        print("2. Tambah Item")
        print("3. Update Stok")
        print("4. Cari Termahal")
        print("5. Total Nilai Inventaris")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if pilihan == "1":
            tampilkan_inventaris(inventaris)
        elif pilihan == "2":
            nama = input("Masukkan nama item: ")
            stok = int(input("Masukkan jumlah stok: "))
            harga = int(input("Masukkan harga: "))
            tambah_item(inventaris, nama, stok, harga)
        elif pilihan == "3":
            nama = input("Masukkan nama item: ")
            jumlah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
            update_stok(inventaris, nama, jumlah)
        elif pilihan == "4":
            item_termahal = cari_termahal(inventaris)
            if item_termahal:
                print(f"Item termahal: {item_termahal['nama']}, Harga: {item_termahal['harga']}")
            else:
                print("Inventaris masih kosong.")
        elif pilihan == "5":
            total = total_nilai(inventaris)
            print(f"Total nilai inventaris: {total}")
        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi inventaris toko. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
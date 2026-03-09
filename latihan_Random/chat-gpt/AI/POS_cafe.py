menu = {
    '1': {'nama': 'Kopi Hitam', 'harga': 15000},
    '2': {'nama': 'Cappuccino', 'harga': 20000},
    '3': {'nama': 'Latte', 'harga': 22000},
    '4': {'nama': 'Roti Bakar', 'harga': 18000},
    '5': {'nama': 'Pisang Goreng', 'harga': 15000},
    '6': {'nama': 'Air Mineral', 'harga': 8000}
}

# menampilkan menu
def tampilkan_menu():
    print("======= Menu Cafe ========")
    for kode, item in menu.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']:,}")

def fungsi_utama():
    total = 0
    pesanan = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (kode) atau ketik 'selesai' untuk bayar :").strip()
        if pilihan.lower() == 'selesai':
            break

        if pilihan in menu:
            qty = int(input(f"Berapa banyak {menu[pilihan]['nama']} : ?"))
            item = menu[pilihan]
            subtotal = item['harga'] * qty
            pesanan.append((item['nama'], item['harga'], qty, subtotal))
            total += subtotal
            print(f"ini adalah total {total}")
            print(f"Ditambahkan: {qty} X {item['nama']} = Rp{subtotal:,}\n")
        else:
            print("Kode menu tidak di temukan, coba lagi.\n")

    print("====STRUK PEMBAYARAN=====")
    for nama, harga, qty, subtotal in pesanan:
        print(f"{nama} ({qty} X Rp{harga:,} = Rp{subtotal:,})")
    print(f"Total bayar : Rp{total:,}")
    print("TERIMAKASIH TELAH BERKUNJUNG")

# MENJALANKAN PROGRAM
if __name__ == "__main__":
    fungsi_utama()
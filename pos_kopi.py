from formatString import harga


def tampilkan_menu(daftar_menu):
    """
    Fungsi untuk menampilkan menu.
    Parameter: daftar_menu (tipe: dictionary)
    """
    print("\n" + "=" * 20)
    print("   MENU KOPI KITA   ")
    print("=" * 20)
    for item, harga in daftar_menu.items():
        # format string agar rapi
        print(f"- {item.ljust(15)}: Rp {harga:,}")
    print("=" * 20)


def hitung_total(harga_satuan, jumlah_beli):
    """
    fungsi untuk menghitung totl harga
    Args:
        harga_satuan:
        jumlah_beli:

    Returns:

    """
    return harga_satuan * jumlah_beli

def proses_pembayaran(total_tagihan, uang_pelanggan):
    """
    fungsi untuk memproses pembayarran dan kembalian
    Args:
        total_tagihan:
        uang_pelanggan:

    Returns:

    """
    if uang_pelanggan >= total_tagihan:
        kembalian = uang_pelanggan - total_tagihan
        print(f"\n✅ Pembayaran Berhasil!")
        print(f"   Total Bayar : Rp {total_tagihan:,}")
        print(f"   Uang Masuk  : Rp {uang_pelanggan:,}")
        print(f"   Kembalian : Rp {kembalian:,}")
    else:
        kurang = total_tagihan - uang_pelanggan
        print(f"\n❌ Uang tidak cukup. Kurang Rp {kurang:,}")

# program utama
# data menu (dictionary)
menu_kopi = {
    "Espresso": 15000,
    "Americano": 1,
    "Latte": 22000,
    "Cappuccino": 25000,
    "Mocha": 28000,
}

# 1. panggil fungsi dengan parameter dictionary
tampilkan_menu(menu_kopi)

# input dari pengguna
pilihan = input("\nMasukkan nama kopi yang dipesan (sesuai menu): ").capitalize()
qty = int(input("Masukkan jumlah pesanan: "))

# validasi apakah menu ada
if pilihan in menu_kopi:
    harga_per_cup = menu_kopi[pilihan]
    total_bayar = hitung_total(harga_per_cup, qty)
    print(f"\nTotal yang harus dibayar: Rp {total_bayar}")
    bayar = int(input("Masukkan uang pembayaran: Rp "))

    # 3. panggil fungsi pembayaran dengan parameter total dan uang
    proses_pembayaran(total_bayar, bayar)
else:
    print("\nMaaf, menu tersebut tidak tersedia.")
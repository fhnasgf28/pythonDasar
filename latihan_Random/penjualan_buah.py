# buat daftar nama dan harga buah
fruits = [("Apel", 5000), ("Jeruk", 8500), ("Mangga", 7800), ("Durian", 6500)]

# buat fungsi untuk menampilkan daftar buah
def display_fruits():
    print("Daftar Buah\t:")
    for i, fruit in enumerate(fruits):
        print(f"{i + 1}. {fruit[0]} - Rp{fruit[1]}")

# buat fungsi untuk memproses pembelian
def process_purchase():
    #  Tampilkan daftar buah
    display_fruits()

    # minta input dari pengguna
    fruit_index = int(input("Pilih Buah yang ingin dibeli (masukan nomor)\t:"))
    fruit_quantity = int(input("Masukan Jumlah yang ingin dibeli\t:"))

    # cari buah yang dipilih
    chosen_fruit = fruits[fruit_index - 1]

    # hitung total harga
    total_price = chosen_fruit[1] * fruit_quantity

    # tampilkan total harga
    print(f"Total Harga\t: Rp{total_price}")

# panggil fungsi untuk memproses pembelian
process_purchase()
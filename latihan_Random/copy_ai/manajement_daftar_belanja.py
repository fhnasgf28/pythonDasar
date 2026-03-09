daftar_belanja = []


def tambah_item(nama, jumlah, harga_satuan):
    daftar_belanja.append((nama, jumlah, harga_satuan))
    print("Item belanja berhasil di tambahkan")


def subtotal_item(item):
    # menghitung subtotal harga untuk satu item
    return item[1] * item[2]


def total_belanja():
    total = 0
    for item in daftar_belanja:
        total += subtotal_item(item)
    return total


def tampilkan_daftar_belanja():
    # menampilkan semua item belanja
    print("Daftar Belanja:")
    for i, item in enumerate(daftar_belanja, start=1):
        print(
            f"{i}. {item[0]} - jumlah: {item[1]}, harga satuan  Harga Satuan: {item[2]}, Subtotal: {subtotal_item(item)}")


# tambahkan beberapa contoh item belanja
tambah_item("Apel", 4, 5000)
tambah_item("Sabun Mandi", 4, 6000)
tambah_item("Sikat Gigi", 1, 30000)

# Tampilkan total belanja dan daftar belanja
print(f"Total Belanja : {total_belanja()}")
tampilkan_daftar_belanja()

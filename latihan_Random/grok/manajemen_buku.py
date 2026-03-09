from formatString import harga

inventaris = {
    "Python for Beginners": {"harga": 150000, "stok": 10},
    "Data Science 101": {"harga": 200000, "stok": 5},
    "Algoritma Dasar": {"harga": 120000, "stok": 8}
}

def proses_pesanan(pesanan):
    total_sebelum_diskon = 0
    ringkasan = []

    # memeriksa setiap item dalam pesanan
    for buku, jumlah in pesanan.items():
        if buku not in inventaris:
            ringkasan.append(f"- {buku}: {jumlah} buah - Buku tidak tersedia di inventaris")
            continue

        stok = inventaris[buku]["stok"]
        harga = inventaris[buku]["harga"]

        if stok >= jumlah:
            total_sebelum_diskon += harga * jumlah
            inventaris[buku]["stok"] -= jumlah
            ringkasan.append(f"- {buku}: {jumlah} buah - Berhasil")
        else:
            ringkasan.append(f"- {buku}: {jumlah} buah - Stok tidak cukup (sisa: {stok})")

    # menghitung diskon
    diskon = 0
    if total_sebelum_diskon > 500000:
        diskon = total_sebelum_diskon * 0.1
    total_setelah_diskon = total_sebelum_diskon - diskon

    # menampilkan ringkasan pesanan
    print("pesanan:")
    for item in ringkasan:
        print(item)

    print(f"\nTotal sebelum diskon: Rp{total_sebelum_diskon:,}")
    if diskon > 0:
        print(f"diskon 10% diterapkan: Rp {diskon:,}")
    print(f"total setelah diskon: Rp {total_setelah_diskon:,}")

    # menampilkan stok terbaru
    print("\nstok terbaru:")
    for buku, info in inventaris.items():
        print(f"- {buku}: {info['stok']}")

# contoh penggunaan
pesanan = {
    "Python for Beginners": 2,
    "Data Science 101": 1,
    "Algoritma Dasar": 3,
    "Machine Learning": 1
}

proses_pesanan(pesanan)
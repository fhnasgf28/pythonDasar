produk = {
    "Produk A": {"jumlah_terjual": 50, "harga_per_unit": 20000},
    "Produk B": {"jumlah_terjual": 30, "harga_per_unit": 15000},
    "Produk C": {"jumlah_terjual": 20, "harga_per_unit": 10000}
}


# fungsi untuk menghitung total pendapatan
def hitung_total_pendapatan(produk):
    total_pendapatan = 0
    for item, data in produk.items():
        pendapatan = data["jumlah_terjual"] * data["harga_per_unit"]
        total_pendapatan += pendapatan
        print(f"Pendapatan dari {item}: Rp {pendapatan}")
    return total_pendapatan


total_pendapatan = hitung_total_pendapatan(produk)
print(f"total pendapatan keseluruhan: Rp {total_pendapatan}")

transaksi = []


def tambah_transaksi(nama, jenis, nominal):
    # menambahkan transaksi baru ke list transaksi
    transaksi.append((nama, jenis, nominal))
    print("Transaksi berhasil di tambahkan")


def total_pemasukan():
    # menghitung total pemasukan
    total = 0
    for t in transaksi:
        if t[1] == 'pemasukan':
            total += t[2]
    return total


def total_pengeluaran():
    # menghitung total pengeluaran
    total = 0
    for t in transaksi:
        if t[1] == 'pengeluaran':
            total += t[2]
    return total


def saldo_terakhir():
    # menampilkan semua transaksi keuangan
    return total_pemasukan() - total_pengeluaran()


def tampilkan_transaksi():
    print("Daftar Transaksi:")
    for i, t in enumerate(transaksi, start=1):
        print(f"{i}. nama: {t[0]},Jenis: {t[1]}, Nominal: {t[2]}")


# tambahkan beberapa contoh transaksi
tambah_transaksi("Gaji", "pemasukan", 300000)
tambah_transaksi("Beli Makanan", "pengeluaran", 100000)
tambah_transaksi("Beli Buku", "pengeluaran", 50000)

# tampilkan saldo terakhir dan daftar transaksi
print(f"Saldo Terakhir: {saldo_terakhir()}")
tampilkan_transaksi()

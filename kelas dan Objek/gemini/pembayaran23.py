class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Pembayaran:
    def __init__(self, barang, jumlah, metode_pembayaran):
        self.barang = barang
        self.jumlah = jumlah
        self.metode_pembayaran = metode_pembayaran

    def hitung_total(self):
        total = self.barang.harga * self.jumlah
        return total

    def hitung_diskon(self):
        total = self.hitung_total()
        if total >= 100000:
            diskon = total * 0.1
        elif total >= 50000:
            diskon = total * 0.05
        else:
            diskon = 0
        return diskon

    def hitung_pajak(self, pajak_persen=10):
        total_sebelum_diskon = self.hitung_total()
        pajak = total_sebelum_diskon * pajak_persen / 100
        return pajak


    def hitung_bayar(self):
        total = self.hitung_total()
        diskon = self.hitung_diskon()
        pajak = self.hitung_pajak()
        bayar = total - diskon + pajak
        return bayar

# contoh penggunan
barang1 = Barang("Buku", 20000)
pembayaran1 = Pembayaran(barang1, 5, "Tunai")

total_bayar = pembayaran1.hitung_bayar()
print("Total Bayar: ", total_bayar)

# menampilkan informasi pembayaran
print("Rincian Pembayaran:")
print("Barang:", pembayaran1.barang.nama)
print("Jumlah:", pembayaran1.jumlah)
print("Methode Pembayaran:", pembayaran1.metode_pembayaran)
print("Total Bayar", pembayaran1.hitung_bayar())

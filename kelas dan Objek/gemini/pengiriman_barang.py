class Barang:
    def __init__(self, nama, harga, kuantitas):
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas


class Pesanan:
    def __init__(self, id_pesanan, tanggal_pemesanan, barang, alamat, kurir):
        self.id_pesanan = id_pesanan
        self.tanggal_pemesanan = tanggal_pemesanan
        self.barang = barang
        self.alamat = alamat
        self.kurir = kurir
        self.status = "Dalam Proses"

    def ubah_status(self, status_baru):
        self.status = status_baru


class Kurir:
    def __init__(self, id_kurir, nama, kendaraan):
        self.id_kurir = id_kurir
        self.nama = nama
        self.kendaraan = kendaraan


def buat_pesanan(id_pesanan, tanggal_pemesanan, barang, alamat, kurir):
    pesanan = Pesanan(id_pesanan, tanggal_pemesanan, barang, alamat, kurir)
    return pesanan

def ubah_status_peanan(pesanan, status_baru):
    pesanan.ubah_status(status_baru)


# contoh penggunaan
barang1 = Barang("Buku", 20000, 2)
barang2 = Barang("Pena", 80000, 5)

# Membuat Kurir
Kurir1 = Kurir("KR001", "Andi", "Motor")

# membuat pesanan
pesanan1 = buat_pesanan("PS001", "2023-11-22", [barang1, barang2], "Jl. Sudirman", Kurir1)

ubah_status_peanan(pesanan1, "Dikirim")
print(pesanan1.status)
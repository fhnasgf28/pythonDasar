class Paket:
    def __init__(self, id_paket, nama_pelanggan, status_pengiriman="dalam perjalanan"):
        self.id_paket = id_paket
        self.nama_pelanggan = nama_pelanggan
        self.status_pengiriman = status_pengiriman

    def update_status(self, status_baru):
        self.status_pengiriman = status_baru

# membuat daftar paket
daftar_paket = [
    Paket(101, "Ali", "Dikirim"),
    Paket(102, "Budi", "Dalam Perjalanan"),
    Paket(103, "Citra", "Tertunda"),
    Paket(104, "Dewi", "Sampai Tujuan"),
]

def tampilkan_paket():
    print("daftar pengiriman")
    for paket in daftar_paket:
        print(f"ID Paket: {paket.id_paket}")
        print(f"Nama Pelanggan: {paket.nama_pelanggan}")
        print(f"Status Pengiriman: {paket.status_pengiriman}")
        print(
            "-----------------"
        )

def update_status_paket(id_paket, status_baru):
    for paket in daftar_paket:
        if paket.id_paket == id_paket:
            paket.update_status(status_baru)
            print("Status pengiriman berhasil diperbarui.")
            return
    print("ID paket tidak ditemukan.")

def laporan_pengiriman():
    laporan = {}
    for paket in daftar_paket:
        laporan[paket.status_pengiriman] = laporan.get(paket.status_pengiriman, 0) + 1
        print("ini adalah mantap",laporan[paket.status_pengiriman])
    for status, jumlah in laporan.items():
        print(f"{status}: {jumlah}")

tampilkan_paket()
update_status_paket(101, "Sampai Tujuan")
laporan_pengiriman()

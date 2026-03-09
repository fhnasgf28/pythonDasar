from latihan_Random.copilot.menghitung_penjualan import total_pendapatan


class Item:
    def __init__(self, nama, harga, jumlah_terjual):
        self.nama = nama
        self.harga = harga
        self.jumlah_terjual = jumlah_terjual

    def hitung_pendapatan(self):
        return self.harga * self.jumlah_terjual

class Cafe:
    def __init__(self, nama_kafe):
        self.nama_kafe = nama_kafe
        self.items = []


    def tambah_item(self, item):
        self.items.append(item)

    def hitung_total_pendapatan(self):
        return sum(item.hitung_pendapatan() for item in self.items)

    def hitung_pajak(self, persen_pajak=10):
        return self.hitung_total_pendapatan() * persen_pajak / 100

    def tampilkan_laporan(self):
        """Menampilkan laporan pendapatan kafe."""
        print(f"\n=== Laporan Pendapatan {self.nama_kafe} ===")
        total_pendapatan = self.hitung_total_pendapatan()
        pajak = self.hitung_pajak()
        total_setelah_pajak = total_pendapatan + pajak

        for item in self.items:
            print(f"{item.nama} - Harga: {item.harga}, Jumlah Terjual: {item.jumlah_terjual}, Total: {item.hitung_pendapatan()}")

        print("=" * 40)
        print(f"Total pendapatan sebelum pajak: Rp{total_pendapatan:,.2f}")
        print(f"Pajak (10%): Rp{pajak:,.2f}")
        print(f"Total pendapatan setelah pajak: Rp{total_setelah_pajak:,.2f}")
        print("=" * 40)

# ======= Contoh Penggunaan Program =======
cafe_saya = Cafe("Kafe Kopi Senja")

jumlah_item = int(input("Masukkan jumlah jenis item yang dijual: "))

for i in range(jumlah_item):
    nama = input(f"Masukkan nama item ke-{i + 1}: ")
    harga = float(input(f"Masukkan harga per unit {nama}: "))
    jumlah_terjual = int(input(f"Masukkan jumlah {nama} yang terjual: "))

    item = Item(nama, harga, jumlah_terjual)
    cafe_saya.tambah_item(item)

# Tampilkan laporan pendapatan
cafe_saya.tampilkan_laporan()

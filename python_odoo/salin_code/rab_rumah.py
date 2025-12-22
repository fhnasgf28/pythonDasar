import locale

try:
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

#
# 1. CLASS MATERIAL (bahan bangungan)
class Material:
    def __init__(self, nama, harga_satuan, jumlah, satuan="pcs"):
        self.nama = nama
        self.harga_satuan = harga_satuan
        self.jumlah = jumlah
        self.satuan = satuan

    def hitung_total(self):
        return self.harga_satuan * self.jumlah

    def __str__(self):
        return f"{self.nama} ({self.satuan}) @ {format_rupiah(self.harga_satuan)}"

class Pekerja:
    def __init__(self, peran, gaji_harian, durasi_kerja):
        self.peran = peran
        self.gaji_harian = gaji_harian
        self.durasi_kerja = durasi_kerja

    def hitung_gaji_total(self):
        return self.gaji_harian * self.durasi_kerja

    def __str__(self):
        return f"{self.peran} ({self.durasi_kerja} hari) @ {format_rupiah(self.gaji_harian)}/hari"


# class proyek rumah (main controller)
class ProyekRumah:
    def __init__(self, nama_proyek, budget_limit, **detail_tambahan):
        self.nama_proyek = nama_proyek
        self.budget_limit = budget_limit
        self.detail = detail_tambahan
        self.list_material = []
        self.list_pekerja = []

    def tambah_material(self, *args):
        for item in args:
            if isinstance(item, Material):
                self.list_material.append(item)
            else:
                print(item)

    # menggunakan *args untuk pekerja juga
    def tambah_pekerja(self, *args):
        for orang in args:
            if isinstance(orang,Pekerja):
                self.list_pekerja.append(orang)

    def hitung_total_biaya(self):
        total_material = sum(m.hitung_total() for m in self.list_material)
        total_pekerja = sum(p.hitung_gaji_total() for p in self.list_pekerja)
        return total_material, total_pekerja, total_material + total_pekerja

    def tampilkan_laporan(self):
        print("="*50)
        print(f"Proyek: {self.nama_proyek.upper()}")

        if self.detail:
            for key, value in self.detail.items():
                print(f"{key.capitalize()}: {value}")

        print("="*50)

        print("\n ---- rincian Material")
        for m in self.list_material:
            print(f"{m}: {format_rupiah(m.hitung_total())}")

        print("\n ---- rincian tenaga kerja")
        for p in self.list_pekerja:
            print(f"{p}: {format_rupiah(p.hitung_gaji_total())}")


        tot_mat, tot_pek, grand_total = self.hitung_total_biaya()
        print("-" * 50)
        print(f"Total Material : {format_rupiah(tot_mat)}")
        print(f"Total Upah     : {format_rupiah(tot_pek)}")
        print(f"GRAND TOTAL    : {format_rupiah(grand_total)}")

        # Logika Bisnis: Cek Budget
        sisa = self.budget_limit - grand_total
        status = "AMAN (Surplus)" if sisa >= 0 else "OVER BUDGET (Defisit)"

        print(f"Budget Awal    : {format_rupiah(self.budget_limit)}")
        print(f"Status Keuangan: {status} sebesar {format_rupiah(abs(sisa))}")
        print("=" * 50)


        # implemantasi / cara pakai
        # inisialisasi objek material
semen = Material("Semen tiga roda", 65000, 50, "sak")
pasir = Material("Pasir Beton", 350000, 3, "pick-up")
bata = Material("Bata Merah", 800, 2000, "pcs")
cat = Material("cat tembok putih", 150000, 5, "kaleng")

# inisialisasi objek pekerja
mandor = Pekerja("Mandor Utama", 200000, 14)
tukang = Pekerja("Tukang Batu", 150000, 10)
tukang_1 = Pekerja("Tukang Batu", 150000, 10)


# 3. Membuat Proyek (Penerapan **kwargs di sini: Lokasi & Pemilik)
rumah_impian = ProyekRumah(
    "Renovasi Dapur Minimalis",
    budget_limit=15000000,
    lokasi="Jakarta Selatan",
    pemilik="Bapak Budi",
    kontraktor="PT Bangun Jaya"
)

# 4. Memasukkan Data (Penerapan *args di sini)
rumah_impian.tambah_material(semen, pasir, bata, cat)
rumah_impian.tambah_pekerja(mandor, tukang, tukang_1)

# 5. Cetak Laporan
rumah_impian.tampilkan_laporan()

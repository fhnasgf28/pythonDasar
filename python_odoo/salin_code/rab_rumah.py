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
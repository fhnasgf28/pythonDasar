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
        return f""


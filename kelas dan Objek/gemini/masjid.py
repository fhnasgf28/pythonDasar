class Masjid:
    def __init__(self, nama, alamat, jumlah_pengurus):
        self.nama = nama
        self.alamat = alamat
        self.jumlah_pengurus = jumlah_pengurus
        self.pengurus = []

    def tambah_pengurus(self, pengurus):
        self.pengurus.append(pengurus)

class Pengurus:
    def __init__(self, nama, nomor_telepon, jabatan):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.jabatan = jabatan

        # membuat objeck msjid

masjid_alhikmh = Masjid("Al-Hikmah", "Jl. sudirman", 5)

        # membuat objek pengurus
pengurus1 = Pengurus("Ahmad", "087988454", "Ketua DKM")
masjid_alhikmh.tambah_pengurus(pengurus1)

print("-----------------------------------")
print("Informasi Masjid Al-Hikmah")
print("-----------------------------------")
print(f"Nama: {masjid_alhikmh.nama}")
print(f"Alamat: {masjid_alhikmh.alamat}")
print(f"Jumlah Pengurus: {masjid_alhikmh.jumlah_pengurus}")

print("\nDaftar Pengurus:")
for pengurus in masjid_alhikmh.pengurus:
    print(f"- {pengurus.nama} ({pengurus.jabatan})")
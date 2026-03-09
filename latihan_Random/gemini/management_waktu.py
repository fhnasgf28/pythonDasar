import datetime


def hitung_selisih_waktu(tanggal_awal, tanggal_ahir):
    format_tanggal = "%Y-%m-%d"
    tanggal_awal = datetime.datetime.strptime(tanggal_awal, format_tanggal)
    tanggal_ahir = datetime.datetime.strptime(tanggal_ahir, format_tanggal)
    selisih = tanggal_ahir - tanggal_awal
    return selisih.days


tanggal_mulai = "2023-11-24"
tanggal_selesai = "2023-12-02"
hasil = hitung_selisih_waktu(tanggal_mulai, tanggal_selesai)
print("Selisih waktu :", hasil, "hari")

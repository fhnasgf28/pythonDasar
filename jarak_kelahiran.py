from datetime import datetime

# format tanggal: YYYY-MM-DD
tanggal1 = datetime.strptime("1995-06-15", "%Y-%m-%d")
tanggal2 = datetime.strptime("2000-09-20", "%Y-%m-%d")

# hitung selisih
selisih = tanggal2 - tanggal1

print("Jarak dalam hari:", selisih.days)
print("Jarak dalam tahun (perkiraan):", selisih.days // 365)

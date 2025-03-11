# definisi variabel

cycle_count_saat_ini = 480
batas_cycle_count = 1000
hari_per_cycle = 2

# perhitungan sisa cycle count
sisa_cycle_count = batas_cycle_count - cycle_count_saat_ini
jumlah_hari = sisa_cycle_count * hari_per_cycle

# conversi ketahun
hari_per_tahun = 365
total_tahun = jumlah_hari / hari_per_tahun

print("Cycle count saat ini:", cycle_count_saat_ini)
print("Batas cycle count:", batas_cycle_count)
print("Hari per cycle:", hari_per_cycle)
print("Total tahun:", total_tahun)
print("Sisa cycle count:", sisa_cycle_count)
print("Jumlah hari:", jumlah_hari)
print(f"dibutuhkan {jumlah_hari} hari untuk mencapai batas cycle count")
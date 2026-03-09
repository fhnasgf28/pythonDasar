# Masukkan jarak pada peta (dalam cm)
jarak_peta = 10  # cm

# Masukkan jarak sebenarnya (dalam km)
jarak_sebenarnya = 25  # km (misalnya jarak sebenarnya ke Gunung Ciremai)

# Konversi jarak sebenarnya dari km ke cm
jarak_sebenarnya_cm = jarak_sebenarnya * 100000  # 1 km = 100000 cm

# Hitung skala peta
skala = jarak_peta / jarak_sebenarnya_cm

# Cetak hasil
print(f"Skala peta adalah 1:{int(1/skala)}")

# Meminta input dari pengguna
jarak_tempuh = float(input("Masukkan jarak tempuh (km): "))
efisiensi_bahan_bakar = float(input("Masukkan efisiensi bahan bakar (km/liter): "))

# Menghitung jumlah bensin yang dibutuhkan
jumlah_bensin = jarak_tempuh / efisiensi_bahan_bakar

# Menampilkan hasil
print("Jumlah bensin yang dibutuhkan:", jumlah_bensin, "liter")
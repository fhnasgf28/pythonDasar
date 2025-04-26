def hitung_pertumbuhan(awal, akhir):
    return ((akhir - awal) / awal) * 100

# Contoh penggunaan
kota_x = hitung_pertumbuhan(1000, 1200)
kota_y = hitung_pertumbuhan(500, 800)

print(f"Pertumbuhan kota X: {kota_x:.2f}%")
print(f"Pertumbuhan kota Y: {kota_y:.2f}%")

if kota_x > kota_y:
    print("Kota X lebih produktif")
else:
    print("Kota Y lebih produktif")
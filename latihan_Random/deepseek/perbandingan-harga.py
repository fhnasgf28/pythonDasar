harga_a = 50000
volume_a = 200
harga_per_ml_a = harga_a / volume_a

harga_b = 60000
volume_b = 300
harga_per_ml_b = harga_b / volume_b

print(f"harga per ml barang A = {harga_per_ml_a}")
print(f"harga per ml barang B = {harga_per_ml_b}")

if harga_per_ml_a > harga_per_ml_b:
    print("barang A lebih mahal")
else:
    print("barang B lebih mahal")
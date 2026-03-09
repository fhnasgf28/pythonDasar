import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

jari_jari = float(input("Masukkan jari jari lingkaran:"))
luas = hitung_luas_lingkaran(jari_jari)
keliling = hitung_keliling_lingkaran(jari_jari)

print(f"luas lingkaran: {luas:.2f}")
print(f"keliling lingkaran: {keliling:.2f}")
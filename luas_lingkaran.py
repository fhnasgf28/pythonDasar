import math

def hitung_luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    return luas

jari_jari_lingkaran = 5
luas_lingkaran = hitung_luas_lingkaran(jari_jari_lingkaran)
print(f"Luas Lingkaran dengan jari-jari {jari_jari_lingkaran} adalah {luas_lingkaran:.2f} satuan persegi")

    
def hitung_kata(texs):
    """Menghitung jumlah kata dalam teks"""
    return len(texs.split())

def hitung_frekuensi_kata(teks):
    kata = teks.lower().split()
    frekuensi = {}
    for k in kata:
        frekuensi[k] = frekuensi.get(k, 0) + 1
    return frekuensi

teks = "Ini adalah contoh teks. Teks ini digunakan untuk menghitung jumlah kata dan frekuensi kata."
jumlah_kata = hitung_kata(teks)
print(f"Jumlah kata: {jumlah_kata}")
print(hitung_frekuensi_kata(teks))
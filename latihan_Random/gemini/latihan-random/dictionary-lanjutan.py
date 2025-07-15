import string 


def hitung_frekuensi_kata(teks):
    teks_bersih = teks.lower()
    for tanda_baca in string.punctuation:
        teks_bersih = teks_bersih.replace(tanda_baca, '')
    # memisahkan kata-kata
    kata_kata = teks_bersih.split()
    frekuensi = {}
    for kata in kata_kata:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1
    return frekuensi

# Contoh Penggunaan:
contoh_teks = "Ini adalah contoh teks. Teks ini akan dianalisis. Contoh, contoh!"
hasil_frekuensi = hitung_frekuensi_kata(contoh_teks)
print("Frekuensi Kata:")
print(hasil_frekuensi)

# Contoh penggunaan lain:
teks_panjang = "Belajar Python itu menyenangkan. Python adalah bahasa pemrograman yang powerful. Saya suka belajar Python!"
hasil_frekuensi_panjang = hitung_frekuensi_kata(teks_panjang)
print("\nFrekuensi Kata (Teks Panjang):")
print(hasil_frekuensi_panjang)

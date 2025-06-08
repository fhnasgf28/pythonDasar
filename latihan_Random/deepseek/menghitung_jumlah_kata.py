def hitung_jumlah_kata(kalimat):
    kata = kalimat.split()
    return len(kata)

kalimat = input("Masukkan sebuah kalimat :")
jumlah_kata = hitung_jumlah_kata(kalimat)
print(f"Jumlah kata dalam kalimat: {jumlah_kata}")
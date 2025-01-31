def hitung_kata(kalimat):
    kata = kalimat.split()
    return len(kata)


# contoh pemanggilan fungsi
kalimat = "Ini adalah contoh kalimat"
jumlah_kata = hitung_kata(kalimat)
print(f"Jumlah kata dalam kalimat: {jumlah_kata}")
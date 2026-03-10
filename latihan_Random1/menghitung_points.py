def hitung_poin(total_belanja):
    poin = total_belanja // 10000
    return poin

# input total belanja
total = int(input("Masukkan total belanja (Rp): "))

poin_didapat = hitung_poin(total)

print("Total belanja:", total)
print("Poin yang didapat:", poin_didapat)

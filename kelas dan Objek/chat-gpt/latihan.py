def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat - 1)

    return bilangan

bilangan = 2  # Ganti dengan bilangan yang ingin Anda hitung pangkatnya
pangkat = 3   # Ganti dengan nilai pangkat yang diinginkan
hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')

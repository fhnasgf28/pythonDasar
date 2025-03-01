def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "genap"
    else:
        return "ganji"

bilangan = int(input("Masukkan sebuah bilangan :"))
hasil = cek_ganjil_genap(bilangan)
print(f"Bilangan {bilangan} adalah bilangan {hasil}")
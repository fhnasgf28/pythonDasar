from latihan.perpangkatan import bilangan


def ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return (f"{bilangan} adalah bilangan genap")
    else:
        return (f"{bilangan} adalah bilangan ganjil")

bilangan = int(input("Masukan bilangan\t:"))
hasil = ganjil_genap(bilangan)
print(hasil)
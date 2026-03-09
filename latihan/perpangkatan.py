bilangan = int(input("Masukan Angka yang kamu inginkan"))
pangkat = int(input("Masukan pangkat yang kamu inginkan"))

# hasil = pow(bilangan, pangkat)
#
# print(f"Hasil \t: {hasil}")


# contoh lain

def hitung_pagkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pagkat(bilangan, pangkat - 1)

    return bilangan


hasil = hitung_pagkat(bilangan, pangkat)

print(f"Hasil \t: {hasil}")

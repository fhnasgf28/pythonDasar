""" panjang = int (input("Masukan panjang persegi : "))
lebar = int(input("Masukan lebar persegi : "))

luas = panjang * lebar
keliling = 4 * panjang

print("Luas persegi adalah : ", luas, "m2")
print("Keliling persegi adalah : ", keliling, "m2") """

import json
def hitung_luas_keliling_persegi(panjang, lebar):
    if panjang < 0:
        raise ValueError("Panjang harus positif")
    if lebar < 0:
        raise ValueError("Lebar harus positif")

    # menghitung luas persegi
    luas = panjang * lebar
    keliling = 4 * panjang

    return luas, keliling

def main():
    hasil = []

    while True:
        try:
            panjang = int(input("Masukan Panjang Persegi:"))
            lebar = int(input("Masukan Lebar Persegi:"))
            
            luas, keliling = hitung_luas_keliling_persegi(panjang, lebar)

            # menyimpan hasil perhitungan
            data = {
                "panjng" : panjang,
                "lebar" : lebar,
                "uas" : luas,
                "keliling" : keliling
            }

            hasil.append(data)
            print("Hasil perhitungan telah ditambahkan")
            continue

            with open("hasil.json", "w") as file:
                json.dump(data, file)

            print("Luas Persegi adalah:", luas)
            print("Keliling Persegi adalah:", keliling)

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
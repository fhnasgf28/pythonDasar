# llatihan

# menentukan nilai variabel

""" nama = "bard"
usia = 2024 - 1998 

print ("saat ini usia {nama} adalah {usia}".format(nama = nama, usia = usia)) """

# contoh ke dua

""" saldo = 1000000

penghasilan = 3500000
pengeluaran = 3000000

saldo += penghasilan - pengeluaran

print(f"Saldo saya sekarang adalah Rp{saldo}") """

# latihan 
print("================Latihan==========")

# membuat satu fungsi 
def validasi_angka (prompt):
    while True:
        try:
            angka = float(input(prompt))
            if angka > 0:
                return angka
            else:
                print("Nilai angka harus lebih besar dari 0")
        except:
            print("Nilai yang dimasukan bukan angka.")


panjang = validasi_angka(input("Masukan Panjang:"))
lebar = validasi_angka(input("Masukan Lebar:"))

# hitung luas persegi panjang 
luas = panjang * lebar 
keliling = 2 * (panjang + lebar)

print(f"Luas Persegi panjang adalah {luas} m2")
print(f"Keliling Persegi panjang adalah {keliling} m2")


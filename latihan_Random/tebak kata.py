import random

# daftar kata
kata_kata = ["apel", "pisang", "mangga", "jeruk", "melon"]

# memilih kata secara acak
kata = random.choice(kata_kata)

# jumlah tebakan maksimal
tebakan_maksimal = 5

# menebak kata
tebakan = 0
while tebakan < tebakan_maksimal and tebakan != kata:
    try:
        tebakan = int(input("Masukan Tebakan\t:"))
    except ValueError:
        print("Input tidak valid. Masukan Angka")
        continue
    tebakan_maksimal -= 1
# hasil tebakan
if tebakan == kata:
    print("Selamat ! anda berhasil menebak kata dengan benar")
else:
    print(f'maaf, anda tidak berhasil menebak kata. kata yang benar adalah {kata}')
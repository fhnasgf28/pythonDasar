import random

angka_rahasia = random.randint(1, 100)

print('=' * 20)
print('kami telah memiliki angka, silahkan tebak')
print('=' * 20)

batas_percobaan = 5
for percobaan in range(batas_percobaan):
    jawaban = int(input(f'percobaan: [ {percobaan+1} ] Masukan angka: '))

# membuat perulangan tak terbatas

    if jawaban == angka_rahasia:
        print("selamat, tebakanmu benar")
        break
    else:
        print(
            'Tebakanmu Terlalu',
            'kecil' if jawaban < angka_rahasia else 'besar',
        )
else:
    print(f'sayang sekali, kamu salah menebak sebanyak {batas_percobaan} kali')
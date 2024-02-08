import random 
import os

# Daftar Kata
kata_list = ["apel", "kata", "manusia","mangga", "jeruk", "melon"]

def main():
    #memilih kata 
    kata = random.choice(kata_list)

    # menyembunyikan kata 
    kata_tersembunyi = "_".join(list(kata))

    # perulangan tebakan
    tebakan_salah = 0

    while True:
        os.system("clear")
        print(f"Tebak Kata\t: {kata_tersembunyi}")
        tebakan = input("Masukan Tebakan\t: ")

        if tebakan == kata:
            print("selamat")
            break
        else:
            tebakan_salah += 1
            print("salah, coba lagi")

            # memperbaharui kta tersembunyi
            for i in range(len(kata)):
                if kata[i] == tebakan:
                    kata_tersembunyi = kata_tersembunyi[:i] + kata[i] + kata_tersembunyi[i+1:]

        if tebakan_salah == 3:
            print("Maaf kamu kehabisan tebakan")
            print(f"kata yang benar adalah\t : {kata}")
            break

if __name__ == "__main__":
    main()

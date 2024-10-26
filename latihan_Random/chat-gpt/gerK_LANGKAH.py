kalori_per_langkah = 0.05

def hitung_kalori(jumlah_langkah):
    return jumlah_langkah * kalori_per_langkah

def main():
    try:
        jumlah_langkah = int(input("Masukkan jumlah langkah yang diambil :"))

        if jumlah_langkah < 0:
            print("Jumlah langkah tidak boleh negatif")
            return

        kalori = hitung_kalori(jumlah_langkah)
        print(f"Jumlah langkah: {jumlah_langkah}")
        print(f"Kalori yang terbakar: {kalori:.2f} kalori")

    except ValueError:
        print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
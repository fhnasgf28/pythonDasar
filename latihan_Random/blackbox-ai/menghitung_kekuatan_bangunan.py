def hitung_kekuatan(beban, luas_penampang, faktor_keamanan):
    # menghitung kekuatan struktur
    kekuatan_struktur = beban / luas_penampang
    # menghitung kekuatan yang diizinkan
    kekuatan_diizinkan = kekuatan_struktur / faktor_keamanan

    return kekuatan_struktur, kekuatan_diizinkan

def main():
    # input dari pengguna
    try:
        beban = float(input("Masukkan beban (N) :"))
        luas_penampang = float(input("Masukkan luas penampang (m2)"))
        faktor_keamanan = float(input("Masukkan  faktor keamanan: "))

        # validasi input
        if luas_penampang <= 0 or faktor_keamanan <= 0:
            print("Luas penampang dan faktor keamanan harus lebih besar dari nol.")
            return

        # hitung kekuatan
        kekuatan_struktur, kekuatan_diizinkan = hitung_kekuatan(beban,luas_penampang, faktor_keamanan)

        print(f"Kekuatan Struktur (σ): {kekuatan_struktur:.2f} N/m²")
        print(f"Kekuatan yang Diizinkan: {kekuatan_diizinkan:.2f} N/m²")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")


if __name__ == "__main__":
    main()
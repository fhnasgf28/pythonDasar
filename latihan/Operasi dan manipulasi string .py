def hitung_karakter_unik(teks):
    karakter_unik = set(teks)
    jumlah_karakter_unik = len(karakter_unik)
    return karakter_unik, jumlah_karakter_unik

def main():
    teks = input("Masukan Teks:")
    karakter_unik, jumlah_karakter_unik = hitung_karakter_unik(teks)
    print(f"\njumlah Karakter Unik: {jumlah_karakter_unik}")
    print("Karakter Unik:", " , ".join(karakter_unik))

if __name__ == "__main__":
    main()
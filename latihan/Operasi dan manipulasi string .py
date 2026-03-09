""" def hitung_karakter_unik(teks):
    karakter_unik = set(teks)
    jumlah_karakter_unik = len(karakter_unik)
    return karakter_unik, jumlah_karakter_unik

def main():
    teks = input("Masukan Teks:")
    karakter_unik, jumlah_karakter_unik = hitung_karakter_unik(teks)
    print(f"\njumlah Karakter Unik: {jumlah_karakter_unik}")
    print("Karakter Unik:", " , ".join(karakter_unik))

if __name__ == "__main__":
    main() """


# latihan ke dua

def hitung_jumlah_kata(teks, batas_bawah=None, batas_atas=None):
    # menggunakan split untuk memisahkan kata-kata
    kata = teks.split()
    # filter kata-kata berdasarkan batas panjang
    kata = [kata for kata in kata if (batas_bawah is None or len(kata) >= batas_bawah) and (batas_atas is None or len(kata) <= batas_atas)]
    return len(kata), kata

def main():
    teks = input("Masukan sebuah string: ")
    batas_bawah = int(input("Masukan Batas bawah panjang kata (biarkan kosong untuk tidak ada batas bawah): ") or 0)
    batas_atas = int(input("Masukkan batas atas panjang kata (biarkan kosong untuk tidak ada batas atas): ") or float('inf'))

    jumlah_kata, kata = hitung_jumlah_kata(teks, batas_bawah, batas_atas)
    print(f"\nJumlah kata dalam string: {jumlah_kata}")
    print("kata-kata yang memenuhi kriteria:", " , ".join(kata))

if __name__ == "__main__":
    main()
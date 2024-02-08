def kategori_usia(umur):
    if umur >= 0 and umur <= 4:
        return "Balita", "Balita adalah anak-anak usia awal yang masih dalam tahap perkembangan cepat."
    elif umur >= 5 and umur <= 12:
        return "Anak-anak","Anak-anak biasanya aktif dan penuh dengan energi, sering kali mengeksplorasi dunia di sekitar mereka."
    elif umur >= 13 and umur <= 17:
        return "Remaja", "Remaja adalah masa transisi antara masa kanak-kanak dan dewasa, di mana individu mulai menemukan identitas mereka."
    elif umur  >= 18 and umur <= 59:
        return "Dewasa", "Dewasa adalah masa ketika individu biasanya telah mencapai kemandirian dan bertanggung jawab atas keputusan mereka."
    else:
        return "Lansia", "Lansia adalah orang-orang yang telah mencapai usia lanjut dan mungkin memerlukan perawatan dan perhatian tambahan."


def simpan_riwayat(riwayat):
    with open("Riwayat_Kategori_Usia.txt", "a") as file:
        for kategori,deskripsi in riwayat:
            file.write(f"kategori: {kategori}\n")
            file.write(f"deskripsi: {deskripsi}\n")


def main():
    print("Selamat Datang di program kategori usia")
    riwayat = []

    while True:
        umur = input("Masukan umur anda (atau ketik 'selesai' untuk keluar): ")
        if umur.lower() == "selesai":
            break

        try:
            umur_int = int(umur)
        except ValueError:
            print("Masukan angka saja")
            continue

        kategori, deskripsi = kategori_usia(umur_int)
        riwayat.append((kategori, deskripsi))

        print(f"Anda termasuk dalam kategori {kategori}")
        print(f"Descripsi kategori {deskripsi}\n")

    if riwayat:
        print("Riwayat Kategori Usia :")
        for kategori, _ in riwayat:
            print(f"- {kategori}")

        simpan = input("Apakah Anda ingin menyimpan riwayat kategori usia dalam fil? (ya/tidak): ")
        if simpan == "ya":
            simpan_riwayat(riwayat)
            print("Riwayat kategori usia telah disimpan dalam file 'riwayat_kategori_usia.txt'.")
        else:
            print("Riwayat kategori usia telah dibatalkan")


if __name__ == "__main__":
    main()

def buat_kartu_nama(nama, pekerjaan, email, telepon):
    kartu_nama = f""" 
    ============Kartu Nama ==========
    Nibble Softwork
    =================================

    nama : {nama}
    pekerjaan : {pekerjaan}
    email : {email}
    telepon: {telepon}
    =================================
    """

    return kartu_nama

def main():
    print("Selamat datang di pembuatan Kartu Nama")

    # Input Pengguna

    nama = input("Masukan Nama Anda :")
    pekerjaan = input("Masukan Pekerjaan Anda :")
    email = input("Masukan Email Anda :")
    telepon = input("Masukan Telepon Anda :")

    # Membuat kartu nama
    kartu_nama = buat_kartu_nama(nama, pekerjaan, email, telepon)

    # menampilkan kartu nama
    print("\nini adalah kartu nama anda:")
    print(kartu_nama)

    # menyimpan kartu nama dalam file
    simpan = input("apakah anda ingin menyimpan kartu nama dalam file? (ya/tidak)").lower()
    if simpan == "ya":
        with open("kartu_nama.txt", "w") as file:
            file.write(kartu_nama)
        print("kartu nama anda telah disimpan dalam file kartu_nama.txt")

if __name__ == '__main__':
    main()

data_buku = []
def masukkan_data_buku():
    nama_buku = input("Masukkan judul buku : ")
    penulis = input("Masukkan penulis buku : ")
    tahun_terbit = int(input("Masukkan tahun terbit buku : "))

    data_buku.append((nama_buku, penulis, tahun_terbit))

def cetak_data_buku():
    with open("data_buku.txt", "a") as file:
        for nama_buku, penulis, tahun_terbit in data_buku:
            file.write(f"Nama Buku: {nama_buku}\n")
            file.write(f"Penulis: {penulis}\n")
            file.write(f"Tahun Terbit: {tahun_terbit}\n\n")

def main():
    while True:
        print("======SELAMAT DATANG DI PERPUSTAKAAN======")
        print("1. Masukkan Data Buku")
        print("2. Cetak Data Buku")
        print("3. Exit")

        pilihan = int(input("Masukkan pilihan (1,2,3): "))
        if pilihan == 1:
            masukkan_data_buku()
        elif pilihan == 2:
            cetak_data_buku()
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

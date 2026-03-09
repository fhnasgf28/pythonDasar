# program list buku

list_buku = []
while True:
    print("======SELAMAT DATANG DI PERPUSTAKAAN======")
    judul = input("Masukkan judul buku : \t")
    penulis = input("Masukkan penulis buku : \t")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print('\n,', '='*10, 'Bata Buku', '='*10, '\n')
    for index, buku in enumerate(list_buku):
        print(f"{index+1}. {buku[0]} | {buku[1]}")

    print('\n,', '='*10, 'Bata Buku', '='*10, '\n')

    lanjut = input("Apakah ingin menambahkan buku lagi? (y/n) : ")
    if lanjut == 'y':
        continue
    else:
        break

print("Terimakasih")
def hitung_total_belanja():
    """
    fungsi untuk menghitung total belanja pelanggan
    """

    total_belanja = 0

    while True:
        # menanyakan nama barang
        nama_barang = input("Masukan nama barang (atau 'selesai' untuk selesai)\t:")

        if nama_barang.lower() == "selesai":
            break

        #tanyakan harga barang
        while True:
            try:
                harga_barang = float(input("Masukan Harga Barang:"))
                if harga_barang > 0:
                    break
                else:
                    print("Harga harus berupa bilangan positif.")
            except ValueError:
                print("Masukan tidak valid. Harap masukkan angka")

        #tanyakan jumlah barang
        while True:
            try:
                jumlah_barang = int(input("Masukkan Jumlah Barang: "))
                if jumlah_barang > 0:
                    break
                else:
                    print("Jumlah harus berupa bilangan bulat positif")
            except ValueError:
                print("Masukkan tidak valid. Harap masukan angka")

        subtotal = harga_barang * jumlah_barang
        total_belanja += subtotal

        #         tampilkan subtotal
        print(f"{nama_barang} x {jumlah_barang} = Rp{subtotal: .2f}")
    print(f"\nTotal Belanja Rp.{total_belanja}")


hitung_total_belanja()

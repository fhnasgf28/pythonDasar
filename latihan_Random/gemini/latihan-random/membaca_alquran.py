def hitung_waktu_baca_alquran(lembar_per_hari=5):
    jumlah_lembar_alquran = 304
    jumlah_halaman_alquran = jumlah_lembar_alquran * 2

    if lembar_per_hari <= 0:
        print(f"Jumlah halaman per hari harus lebih dari 0")
        return

    hari_dibutuhkan = jumlah_halaman_alquran / (lembar_per_hari * 2)
    minggu_dibutuhkan = hari_dibutuhkan / 7
    bulan_dibutuhkan = hari_dibutuhkan / 30.44

    print(f"jumlah total halam alquran {jumlah_halaman_alquran}")
    print(f"jumlah lembar alquran {jumlah_lembar_alquran}")
    print(f"jumlah halaman per hari {lembar_per_hari}")
    print(f"jumlah hari dibutuhkan {hari_dibutuhkan}")
    print(f"jumlah minggu dibutuhkan {minggu_dibutuhkan}")
    print(f"jumlah bulan dibutuhkan {bulan_dibutuhkan}")

hitung_waktu_baca_alquran(lembar_per_hari=5)
def buat_kue():
    langkah_langkah = [
        "1. Menyiapkan bahan-bahan",
        "2. Mencampur bahan utama",
        "3. Mengaduk adonan hingga merata",
        "4. Menuangkan adonan ke dalam loyang",
        "5. Memanaskan oven",
        "6. Memanggang kue di dalam oven",
        "7. Mengeluarkan kue dari oven",
        "8. Mendinginkan dan menyajikan kue"
    ]

    print("\n=== Proses Pembuatan Kue ===")

    for langkah in langkah_langkah:
        print(langkah)

    print("Kue telah selesai dibuat! 🍰\n")

while True:
    buat_kue()
    ulangi = input("Apakah ingin membuat kue lagi? (ya/tidak) ")
    if ulangi.lower() != 'ya':
        break

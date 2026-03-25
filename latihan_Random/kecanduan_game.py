def deteksi_kecanduan_game():
    print("=== Alat skrining Mandiri kecanduan Game ===")
    print("jawab pertanyaan berikut dengan skala 1-5")
    pertanyaan = [
        "Apakah Anda merasa gelisah saat tidak bisa bermain game?",
        "Apakah Anda sering gagal mengurangi waktu bermain game?",
        "Apakah Anda kehilangan minat pada hobi lain karena game?",
        "Apakah Anda berbohong kepada orang lain tentang durasi bermain?",
        "Apakah game mengganggu sekolah, pekerjaan, atau hubungan sosial Anda?",
        "Apakah Anda menggunakan game untuk melarikan diri dari masalah hidup?"
    ]
    skor_total = 0 

    for i, q in enumerate(pertanyaan):
        while True:
            try:
                skor = int(input(f"{i +1}. {q}"))
                if 1 <= skor <= 5:
                    skor_total += skor
                    break
                else:
                    print(("Mohon masukkan angka antara 1 sampai 5"))
            except ValueError:
                print("Input harus berupa angka.")

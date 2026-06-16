def deteksi_kecanduan_game():
    print("=== Alat Skrining Mandiri Kecanduan Game ===")
    print("Jawab pertanyaan berikut dengan skala 1-5:")
    print("1: Tidak Pernah | 2: Jarang | 3: Kadang-kadang | 4: Sering | 5: Sangat Sering\n")

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
                skor = int(input(f"{i+1}. {q} "))
                if 1 <= skor <= 5:
                    skor_total += skor
                    break
                else:
                    print("Mohon masukkan angka antara 1 sampai 5.")
            except ValueError:
                print("Input harus berupa angka.")

    print("\n--- Hasil Analisis ---")
    print(f"Total Skor Anda: {skor_total} / {len(pertanyaan) * 5}")

    if skor_total <= 12:
        status = "Risiko Rendah: Hubungan Anda dengan game masih sehat."
    elif 13 <= skor_total <= 20:
        status = "Risiko Sedang: Waspada, Anda mulai menunjukkan tanda-tanda ketergantungan."
    else:
        status = "Risiko Tinggi: Sangat disarankan untuk berkonsultasi dengan profesional (psikolog/konselor)."

    print(f"Status: {status}")

if __name__ == "__main__":
    deteksi_kecanduan_game()

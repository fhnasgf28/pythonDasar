def hitung_persentase_kesuksesan(usaha, keterampilan, jaringan, waktu, faktor_keberuntungan=0.1):
    """
    Menghitung persentase kesuksesan berdasarkan faktor-faktor umum orang menengah.

    usaha: 0-10 (berapa keras kamu bekerja)
    keterampilan: 0-10 (skill dan kompetensi)
    jaringan: 0-10 (seberapa baik koneksi dan relasi kamu)
    waktu: 0-10 (berapa lama kamu konsisten)
    faktor_keberuntungan: 0-1 (default 0.1 = 10%)
    """

    # Bobot asumsi untuk orang menengah
    bobot_usaha = 0.35
    bobot_keterampilan = 0.3
    bobot_jaringan = 0.2
    bobot_waktu = 0.15

    skor = (
        usaha * bobot_usaha +
        keterampilan * bobot_keterampilan +
        jaringan * bobot_jaringan +
        waktu * bobot_waktu
    )

    # Masukkan faktor keberuntungan
    total = skor * (1 + faktor_keberuntungan)

    # Batasi maksimum 100%
    return min(round(total * 10, 2), 100.0)

# Contoh penggunaan:
persentase = hitung_persentase_kesuksesan(
    usaha=7,          # kamu kerja cukup keras
    keterampilan=6,   # skill sedang berkembang
    jaringan=5,       # koneksi lumayan
    waktu=6           # konsisten sedang-sedang saja
)

print(f"Persentase kesuksesan kamu saat ini: {persentase}%")

import random 

def hitung_peluang_kerja(pendidikan, keterampilan, pengalaman, lapangan_kerja):
    """
    Menghitung peluang kerja berdasarkan faktor-faktor tertentu.

    Args:
        pendidikan (int): Tingkat pendidikan (misalnya, 1 untuk SMA, 2 untuk Diploma, 3 untuk Sarjana).
        keterampilan (int): Jumlah keterampilan yang dimiliki (misalnya, 1-5).
        pengalaman (int): Lama pengalaman kerja dalam tahun.
        lapangan_kerja (int): Ketersediaan lapangan kerja di desa (misalnya, 1-3).

    Returns:
        float: Persentase peluang kerja.
    """
    # bobot untuk setiap faktor
    bobot_pendidikan = 0.3
    bobot_keterampilan = 0.25
    bobot_pengalaman = 0.2
    bobot_lapangan_kerja = 0.25

    # normalisasi nilai faktor
    pendidikan_normalisasi = pendidikan / 3.0
    keterampilan_normalisasi = keterampilan / 5.0
    pengalaman_normalisasi = min(pengalaman / 10.0, 1.0)
    lapangan_kerja_normalisasi = lapangan_kerja / 3.0

    # hitung skor peluang kerja
    skor = (bobot_pendidikan * pendidikan_normalisasi +
            bobot_keterampilan * keterampilan_normalisasi +
            bobot_pengalaman * pengalaman_normalisasi +
            bobot_lapangan_kerja * lapangan_kerja_normalisasi)

    # konversi skor menjadi persentase 
    peluang = skor * 100 
    return peluang

# Contoh penggunaan
pendidikan = 2  # Diploma
keterampilan = 4
pengalaman = 2
lapangan_kerja = 2

peluang_kerja = hitung_peluang_kerja(pendidikan, keterampilan, pengalaman, lapangan_kerja)
print(f"Peluang kerja: {peluang_kerja:.2f}%")

# simulasi untuk beberapa pemuda 
jumlah_pemuda = 100
pemuda_berhasil = 0

for pemuda in range(jumlah_pemuda):
    pendidikan = random.randint(1, 3)
    keterampilan = random.randint(1, 5)
    pengalaman = random.randint(0, 5)
    lapangan_kerja = random.randint(1, 3)

    peluang_kerja = hitung_peluang_kerja(pendidikan, keterampilan, pengalaman, lapangan_kerja)

persentase_pemuda_berhasil = (pemuda_berhasil / jumlah_pemuda) * 100 
print(f"Persentase pemuda dengan peluang kerja layak: {persentase_pemuda_berhasil:.2f}%")
import random


def ambil_kata_motivasi(file_motivasi):
    """Fungsi untuk mengambil kata-kata motivasi secara acak dari file.

    Args:
      file_motivasi: Nama file yang berisi kata-kata motivasi.

    Returns:
      Kata motivasi yang diambil secara acak.
    """

    with open(file_motivasi, 'r') as file:
        motivasi = file.readlines()
        # Hapus karakter newline di akhir setiap baris
        motivasi = [motivasi.strip() for motivasi in motivasi]

    # Ambil kata motivasi secara acak
    kata_motivasi = random.choice(motivasi)
    return kata_motivasi


# Ganti 'motivasi.txt' dengan nama file Anda
file = 'motivasi.txt'

# Panggil fungsi dan cetak kata motivasi
motivasi_hari_ini = ambil_kata_motivasi(file)
print(motivasi_hari_ini)
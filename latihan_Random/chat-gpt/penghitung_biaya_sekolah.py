from datetime import datetime

# Data untuk biaya sekolah dasar, biaya kelas, dan biaya ekstrakulikuler
BIAYA_DASAR_SEKOLAH = 2000000
BIAYA_KELAS = {
    1: 500000,
    2: 600000,
    3: 700000,
}

EKSTRAKULIKULER = {
    'musik': 300000,
    'olahraga': 250000,
    'seni': 200000
}

DISKON = 0.1
TANGGAL_DISKON = '2024-01-31'

# fungsi untuk menghitung total biaya sekolah
def hitung_biaya_sekolah(kelas, ekstrakulikuler=[], tanggal_pendaftaran=None):
    # biaya dasar sekolah
    total_biaya = BIAYA_DASAR_SEKOLAH
    # tambahkan biaya kelas
    total_biaya += BIAYA_KELAS.get(kelas, 0)

    # tambahkan biaya ekstrakulikuler
    for kegiatan in ekstrakulikuler:
        total_biaya += EKSTRAKULIKULER.get(kegiatan, 0)

    # cek apakah siswa berhak mendapatkan diskon
    if tanggal_pendaftaran:
        tanggal_pendaftaran = datetime.strptime(tanggal_pendaftaran, '%Y-%m-%d')
        tanggal_diskon = datetime.strptime(TANGGAL_DISKON, '%Y-%m-%d')
        if tanggal_pendaftaran <= tanggal_diskon:
            total_biaya -= total_biaya * DISKON

        return total_biaya

    # contoh penggunaan fungsi
if __name__ == "__main__":
    # Data Siswa
    kelas_siswa = 2
    ekstrakulikuler_siswa = ['musik', 'olahraga']
    tanggal_pendaftaran_siswa = '2024-01-20'
    #  menghitung biaya sekolah
    total_biaya = hitung_biaya_sekolah(kelas_siswa, ekstrakulikuler_siswa, tanggal_pendaftaran_siswa)
    print(f"Total biaya sekolah untuk siswa kelas {kelas_siswa} adalah: Rp{total_biaya:,}")
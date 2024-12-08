class Aktivitas:
    def __init__(self, nama, waktu_mulai, waktu_selesai, deskripsi=None):
        self.nama = nama
        self.waktu_mulai = waktu_mulai
        self.waktu_selesai = waktu_selesai
        self.deskripsi = deskripsi

    def __str__(self):
        return f"{self.waktu_mulai} - {self.waktu_selesai}: {self.nama} ({self.deskripsi})"

class JadwalHarian:
    def __init__(self, tanggal):
        """ REPRESNTASI JADWAL HARIAN """
        self.tanggal = tanggal
        self.aktivitas = []

    def tambah_aktivitas(self, aktivitas):
        """Menambahkan aktivitas ke jadwal"""
        if not isinstance(aktivitas, Aktivitas):
            raise ValueError("Aktivitas harus berupa objek Aktivitas")
        self.aktivitas.append(aktivitas)

    def tampilkan_jadwal(self):
        """
        Menampilkan jadwal hari ini
        """
        print(f"Jadwal untuk tanggal {self.tanggal}:")
        if not self.aktivitas:
            print("Tidak ada aktivitas")
        else:
            for aktivitas in sorted(self.aktivitas, key=lambda x: x.waktu_mulai):
                print(f"- {aktivitas}")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat jadwal harian
    jadwal = JadwalHarian("2024-12-01")

    # Menambahkan aktivitas
    jadwal.tambah_aktivitas(Aktivitas("Olahraga", "06:00", "07:00", "Jogging di taman"))
    jadwal.tambah_aktivitas(Aktivitas("Sarapan", "07:30", "08:00"))
    jadwal.tambah_aktivitas(Aktivitas("Bekerja", "09:00", "17:00", "Pekerjaan kantor"))
    jadwal.tambah_aktivitas(Aktivitas("Membaca buku", "20:00", "21:00", "Buku fiksi"))

    # Menampilkan jadwal harian
    jadwal.tampilkan_jadwal()
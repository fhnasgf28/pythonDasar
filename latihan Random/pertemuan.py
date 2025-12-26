from datetime import datetime, timedelta, date


class  Pertemuan:
    def __init__(self, topik,waktu_mulai,durasi_menit=60,peserta=None):
        if not isinstance(waktu_mulai, datetime):
            raise ValueError("waktu mulai harus berupa objek datetime")
        self.topik = topik
        self.waktu_mulai = waktu_mulai
        self.durasi_menit = durasi_menit
        self.peserta = peserta if peserta is not None else []
    
    def dapatkan_waktu_selesai(self):
        return self.waktu_mulai + timedelta(minutes=self.durasi_menit)
    
    def __str__(self):
        """
        mengembalikan representasi string yang mudah dibaca dari objek pertemuan
        digunakan saat objek dicetak (print())
        """
        waktu_selesai_str = self.dapatkan_waktu_selesai.strftime('%H:%M')
        peserta_str = ', ',join(self.peserta) if self.peserta else "Tidak ada"
        return (f"[{self.waktu_mulai.strftime('%Y-%m-%d %H:%M')} - {waktu_selesai_str}]"
        f"topik: {self.topik}"
        f"(durasi: {self.durasi_menit} min, peserta: {peserta_str})"
        )

# kelas jadwal 
class Jadwal:
    """
    mengelola daftar pertemuan, memungkinkan penambahan, tampilan dan pembatalan pertemuan
    """
    def __init__(self):
        """
        konstruktor untuk membuat objek jadwal baru.
        jadwal akan menyimpan daftar objek pertemuan
        """
        self.daftar_pertemuan = []
    
    def tambah_pertemuan(self, pertemuan):
        """
        menambahkan objek pertemuan kedalam jadwal.
        pertemuan akan diurutkan berdasarkan waktu mulai. 
        """
        if not isinstance(pertemuan, Pertemuan):
            raise TypeErrorV("Hanya objek pertemuan yang dapat ditambahkan ke jadwal")
            self.daftar_pertemuan.append(pertemuan)
            self.daftar_pertemuan.sort(key=lambda p: p.waktu_mulai)
            print(f"Pertemuan '{pertemuan.topik}' berhasil ditambahkan")
    
    def lihat_semua_pertemuan(self):
        if not self.daftar_pertemuan:
            print("tidak ada pertemuan yang terjadwal saat ini")
            return 
        print("\n ---- semua pertemuan terjadwal")
        for pertemuan in self.daftar_pertemuan:
            print(pertemuan)
        print("----------------")
    
    def lihat_pertemuan_pada_tanggal(self, tanggal_target):
        """
        menampilkan pertemuan yang terjadwal pada tanggal tertentu.
        args:
        tanggal_target (date): objek date (e.g) yang akan digunakan untk filter
        """
        if not isinstance(tanggal_target, date):
            raise ValueError("tanggal_target harus berupa objek date")
        
        pertemuan_pada_hari = [
            p for p in self.daftar_pertemuan if p.waktu_mulai.date() == tanggal_target
        ]

        if not pertemuan_pada_hari:
            print(f"tidak ada pertemuan terjadwal untk {tanggal_target.strftime('%Y-%m-%d')}")
            return
            
            print(f"\n ---- pertemuan untuk {tanggal_target.strftime('%Y-%m-%d')} ")
            for pertemuan in pertemuan_pada_hari:
                print(pertemuan)
            print("----------------------")

    def batalkan_pertemuan(self, topik, waktu_mulai):
        pertemuan_ditemukan = False 
        daftar_baru = []
        for pertemuan in self.daftar_pertemuan:
            if pertemuan.topik == topik and pertemuan.waktu_mulai:
                print(f"Pertamuan '{topik}' pada {waktu_mulai.strftime('%Y-%m-%d %H:%M')} dibatalkan")
                pertemuan_ditemukan = True
            else:
                daftar_baru.append(pertemuan)
        self.daftar_pertemuan = daftar_baru
        if not pertemuan_ditemukan:
            print(f"Pertemuan dengan topik {topik} pada {waktu_mulai.strftime('%Y-%m-%d %H:%M')} tidak ditemukan")

# bagian program
if __name__ == "__main__":
    # 1. Membuat objek Jadwal
    my_scheduler = Jadwal()

    # 2. Membuat objek Pertemuan
    pertemuan1 = Pertemuan(
        topik="Review Proyek Alpha",
        waktu_mulai=datetime(2023, 11, 15, 10, 0),
        durasi_menit=90,
        peserta=["Alice", "Bob"]
    )

    pertemuan2 = Pertemuan(
        topik="Diskusi Strategi Marketing",
        waktu_mulai=datetime(2023, 11, 16, 14, 30),
        durasi_menit=60,
        peserta=["Charlie", "Diana", "Alice"]
    )

    pertemuan3 = Pertemuan(
        topik="1-on-1 dengan Manajer",
        waktu_mulai=datetime(2023, 11, 15, 13, 0),
        durasi_menit=30
    )
    
    pertemuan4 = Pertemuan(
        topik="Rapat Harian Tim",
        waktu_mulai=datetime(2023, 11, 16, 9, 0),
        durasi_menit=15,
        peserta=["Charlie", "Diana"]
    )

    # 3. Menambahkan pertemuan ke jadwal
    my_scheduler.tambah_pertemuan(pertemuan1)
    my_scheduler.tambah_pertemuan(pertemuan2)
    my_scheduler.tambah_pertemuan(pertemuan3)
    my_scheduler.tambah_pertemuan(pertemuan4)

    # 4. Melihat semua pertemuan
    my_scheduler.lihat_semua_pertemuan()

    # 5. Melihat pertemuan untuk tanggal tertentu
    hari_ini = date(2023, 11, 15)
    my_scheduler.lihat_pertemuan_pada_tanggal(hari_ini)

    besok = date(2023, 11, 16)
    my_scheduler.lihat_pertemuan_pada_tanggal(besok)
    
    # Tanggal yang tidak ada pertemuan
    tidak_ada_pertemuan_tgl = date(2023, 11, 17)
    my_scheduler.lihat_pertemuan_pada_tanggal(tidak_ada_pertemuan_tgl)

    # 6. Membatalkan pertemuan
    print("\n--- Membatalkan Pertemuan ---")
    my_scheduler.batalkan_pertemuan(
        topik="1-on-1 dengan Manajer",
        waktu_mulai=datetime(2023, 11, 15, 13, 0)
    )
    
    # Mencoba membatalkan pertemuan yang tidak ada
    my_scheduler.batalkan_pertemuan(
        topik="Rapat Fiktif",
        waktu_mulai=datetime(2023, 11, 18, 10, 0)
    )

    # 7. Melihat jadwal setelah pembatalan
    my_scheduler.lihat_semua_pertemuan()
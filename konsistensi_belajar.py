import json
import os
import time
from datetime import datetime, date, timedelta
from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRAKSI: Kelas Induk Aktivitas (OOP)
# ==========================================
class AktivitasBelajar(ABC):
    """
    Kelas abstrak yang mendefinisikan struktur dasar dari sebuah aktivitas belajar.
    Menerapkan prinsip Abstraksi dan Encapsulation.
    """
    def __init__(self, nama_topik: str, durasi_menit: int):
        self._nama_topik = nama_topik      # Encapsulation: protected attribute
        self._durasi_menit = durasi_menit  # Encapsulation: protected attribute
        self._tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def nama_topik(self) -> str:
        return self._nama_topik

    @property
    def durasi_menit(self) -> int:
        return self._durasi_menit

    @property
    def tanggal(self) -> str:
        return self._tanggal

    @abstractmethod
    def hitung_exp(self) -> int:
        """Metode abstrak untuk menghitung EXP berdasarkan jenis aktivitas belajar."""
        pass

    @abstractmethod
    def tampilkan_info(self) -> str:
        """Metode abstrak untuk menampilkan representasi string dari aktivitas."""
        pass


# ==========================================
# 2. INHERITANCE & POLYMORPHISM (OOP)
# ==========================================
class SesiCoding(AktivitasBelajar):
    """
    Kelas anak untuk aktivitas coding praktis. Mewarisi AktivitasBelajar.
    Menerapkan prinsip Polimorfisme pada hitung_exp dan tampilkan_info.
    """
    def __init__(self, nama_topik: str, durasi_menit: int, baris_kode: int, bahasa_pemrograman: str):
        super().__init__(nama_topik, durasi_menit)
        self.baris_kode = baris_kode
        self.bahasa_pemrograman = bahasa_pemrograman

    def hitung_exp(self) -> int:
        # Coding memberikan EXP lebih banyak: 15 EXP per menit + bonus dari jumlah baris kode
        bonus_code = min(self.baris_kode // 10, 50)  # Maksimal bonus code 50 EXP
        return (self.durasi_menit * 15) + bonus_code

    def tampilkan_info(self) -> str:
        return (f"[💻 Coding] Topik: {self.nama_topik} ({self.bahasa_pemrograman}) "
                f"| Durasi: {self.durasi_menit} menit | Kode ditulis: ~{self.baris_kode} baris "
                f"| +{self.hitung_exp()} EXP")


class SesiMembaca(AktivitasBelajar):
    """
    Kelas anak untuk aktivitas membaca teori/dokumentasi. Mewarisi AktivitasBelajar.
    Menerapkan prinsip Polimorfisme pada hitung_exp dan tampilkan_info.
    """
    def __init__(self, nama_topik: str, durasi_menit: int, sumber_bacaan: str):
        super().__init__(nama_topik, durasi_menit)
        self.sumber_bacaan = sumber_bacaan

    def hitung_exp(self) -> int:
        # Membaca teori memberikan 10 EXP per menit
        return self.durasi_menit * 10

    def tampilkan_info(self) -> str:
        return (f"[📚 Teori] Topik: {self.nama_topik} (Sumber: {self.sumber_bacaan}) "
                f"| Durasi: {self.durasi_menit} menit | +{self.hitung_exp()} EXP")


# ==========================================
# 3. KELAS USER PROFILE (OOP)
# ==========================================
class UserProfile:
    """
    Kelas untuk menyimpan profil pengguna, level, streak, dan akumulasi EXP.
    Menerapkan prinsip Enkapsulasi penuh dengan properti dan validasi.
    """
    def __init__(self, nama: str):
        self.nama = nama
        self._level = 1
        self._exp = 0
        self._streak = 0
        self._tanggal_terakhir_belajar = None

    @property
    def level(self) -> int:
        return self._level

    @property
    def exp(self) -> int:
        return self._exp

    @property
    def streak(self) -> int:
        return self._streak

    @property
    def tanggal_terakhir_belajar(self):
        return self._tanggal_terakhir_belajar

    def exp_untuk_level_berikutnya(self) -> int:
        """Rumus kenaikan level: Level 1 -> 2 butuh 100 EXP, dst (Level * 150)"""
        return self._level * 150

    def tambah_exp(self, jumlah: int) -> bool:
        """Menambahkan EXP dan mengembalikan True jika naik level."""
        self._exp += jumlah
        naik_level = False
        
        while self._exp >= self.exp_untuk_level_berikutnya():
            self._exp -= self.exp_untuk_level_berikutnya()
            self._level += 1
            naik_level = True
            
        return naik_level

    def perbarui_streak(self):
        """Memperbarui rentetan hari belajar berturut-turut (Streak)."""
        hari_ini = date.today()
        
        if self._tanggal_terakhir_belajar is None:
            self._streak = 1
        else:
            tgl_terakhir = datetime.strptime(self._tanggal_terakhir_belajar, "%Y-%m-%d").date()
            selisih = (hari_ini - tgl_terakhir).days
            
            if selisih == 1:
                self._streak += 1
            elif selisih > 1:
                self._streak = 1  # Streak reset jika terlewat lebih dari 1 hari
            # Jika selisih == 0 (belajar di hari yang sama), streak tidak berubah
            
        self._tanggal_terakhir_belajar = hari_ini.strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        return {
            "nama": self.nama,
            "level": self._level,
            "exp": self._exp,
            "streak": self._streak,
            "tanggal_terakhir_belajar": self._tanggal_terakhir_belajar
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'UserProfile':
        user = cls(data.get("nama", "Pelajar Python"))
        user._level = data.get("level", 1)
        user._exp = data.get("exp", 0)
        user._streak = data.get("streak", 0)
        user._tanggal_terakhir_belajar = data.get("tanggal_terakhir_belajar")
        return user


# ==========================================
# 4. KELAS UTAMA: ConsistencyTracker (OOP)
# ==========================================
class ConsistencyTracker:
    """
    Kelas manajer yang mengatur alur program, pemuatan data, penyimpanan,
    serta integrasi Pomodoro Timer dan statistik belajar.
    """
    def __init__(self, filename='konsistensi_belajar.json'):
        self.filename = filename
        self.user = None
        self.riwayat_sesi = []
        self.load_data()

    def load_data(self):
        """Memuat data profil dan riwayat dari file JSON."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.user = UserProfile.from_dict(data.get("profile", {"nama": "Farhan"}))
                    self.riwayat_sesi = data.get("riwayat", [])
            except Exception as e:
                print(f"[Peringatan] Gagal memuat data lama: {e}. Membuat sesi baru.")
                self.buat_profil_baru()
        else:
            self.buat_profil_baru()

    def save_data(self):
        """Menyimpan seluruh state ke file JSON."""
        data = {
            "profile": self.user.to_dict(),
            "riwayat": self.riwayat_sesi
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def buat_profil_baru(self):
        print("\n=== Selamat Datang di Tracker Konsistensi Belajar OOP ===")
        nama = input("Masukkan nama Anda untuk mulai konsisten belajar: ").strip()
        if not nama:
            nama = "Farhan"
        self.user = UserProfile(nama)
        self.riwayat_sesi = []
        self.save_data()
        print(f"Profil untuk {nama} berhasil dibuat! Tetap konsisten setiap hari ya!\n")

    def catat_aktivitas(self, sesi: AktivitasBelajar):
        """Mencatat aktivitas belajar, menambah EXP, dan memperbarui streak."""
        exp_didapat = sesi.hitung_exp()
        
        # Streak multiplier bonus EXP
        bonus_streak = 0
        if self.user.streak > 1:
            # Bonus 5% EXP ekstra per hari streak (maksimal 50% bonus)
            multiplier = min(self.user.streak * 0.05, 0.50)
            bonus_streak = int(exp_didapat * multiplier)
            
        total_exp = exp_didapat + bonus_streak
        
        # Simpan riwayat sesi ke list
        self.riwayat_sesi.append({
            "info": sesi.tampilkan_info(),
            "exp": total_exp,
            "tanggal": sesi.tanggal,
            "durasi": sesi.durasi_menit
        })
        
        # Perbarui profile user
        self.user.perbarui_streak()
        naik_level = self.user.tambah_exp(total_exp)
        
        print("\n" + "="*50)
        print("🎉 SESI BELAJAR BERHASIL DICATAT!")
        print(sesi.tampilkan_info())
        if bonus_streak > 0:
            print(f"🔥 Bonus Streak ({self.user.streak} Hari): +{bonus_streak} EXP!")
        print(f"Total EXP Diperoleh: +{total_exp} EXP")
        
        if naik_level:
            print(f"\n🌟 LUAR BIASA! Anda naik ke LEVEL {self.user.level}! 🌟")
            print("Setiap jam coding Anda membentuk neuron pemrograman baru. Lanjutkan!")
            
        print("="*50 + "\n")
        self.save_data()

    def tampilkan_dashboard(self):
        """Menampilkan stats belajar, progress bar level, streak, dan riwayat."""
        print("\n" + "="*55)
        print(f"📊 DASHBOARD KONSISTENSI BELAJAR: {self.user.nama.upper()} 📊")
        print("="*55)
        print(f"🔥 Current Streak : {self.user.streak} Hari Berturut-turut")
        print(f"⭐ Level          : {self.user.level}")
        
        # Progress Bar EXP
        exp_skrg = self.user.exp
        exp_target = self.user.exp_untuk_level_berikutnya()
        persen_exp = (exp_skrg / exp_target) * 100
        bar_length = 20
        filled = int(bar_length * exp_skrg // exp_target)
        bar = '█' * filled + '-' * (bar_length - filled)
        print(f"📈 EXP Progress   : |{bar}| {persen_exp:.1f}% ({exp_skrg}/{exp_target} EXP)")
        
        # Kalkulasi Total Waktu
        total_menit = sum(sesi.get("durasi", 0) for sesi in self.riwayat_sesi)
        jam = total_menit // 60
        menit = total_menit % 60
        print(f"⏳ Total Waktu    : {jam} jam {menit} menit ({len(self.riwayat_sesi)} sesi belajar)")
        
        # Tanggal Terakhir Belajar
        tgl_akhir = self.user.tanggal_terakhir_belajar or "Belum belajar"
        print(f"📅 Terakhir Aktif : {tgl_akhir}")
        
        # Rekomendasi/Motivasi
        print("\n💡 Tips Konsistensi Hari Ini:")
        if self.user.streak == 0:
            print("   -> Langkah tersulit adalah memulai. Jalankan 1 sesi Pomodoro sekarang!")
        elif self.user.streak < 3:
            print("   -> Bagus! Pertahankan momentum Anda untuk membangun kebiasaan baru.")
        else:
            print("   -> Luar biasa! Streak Anda terus berkembang. Jangan biarkan rantai terputus!")
            
        print("="*55 + "\n")

    def tampilkan_riwayat(self):
        """Menampilkan seluruh log aktivitas belajar."""
        if not self.riwayat_sesi:
            print("\n📌 Belum ada riwayat sesi belajar. Yuk mulai belajar sekarang!\n")
            return
            
        print("\n" + "-"*65)
        print("📜 RIWAYAT SESI BELAJAR ANDA:")
        print("-"*65)
        for i, sesi in enumerate(reversed(self.riwayat_sesi), 1):
            print(f"{i}. [{sesi['tanggal']}] {sesi['info']}")
        print("-"*65 + "\n")

    def jalankan_pomodoro(self, durasi_menit=25):
        """
        Integrasi Pomodoro Timer untuk melatih fokus belajar secara real-time.
        Setelah timer habis, user dapat langsung mencatat sesi belajar tersebut.
        """
        print("\n" + "="*45)
        print(f"⏱️  MEMULAI TIMER POMODORO ({durasi_menit} MENIT) ⏱️")
        print("Fokus penuh, matikan semua distraksi. Selamat belajar!")
        print("="*45)
        
        detik = durasi_menit * 60
        try:
            while detik > 0:
                menit_sisa = detik // 60
                detik_sisa = detik % 60
                # Tampilkan countdown di baris yang sama
                print(f"\r⏳ Sisa Waktu Fokus: {menit_sisa:02d}:{detik_sisa:02d} | Tekan Ctrl+C untuk menyudahi", end="")
                time.sleep(1)
                detik -= 1
            print("\n\n🔔 WAKTU HABIS! Selamat, Anda menyelesaikan 1 sesi fokus Pomodoro!")
            self._proses_log_otomatis(durasi_menit)
        except KeyboardInterrupt:
            # Jika dibatalkan di tengah jalan, tawarkan untuk mencatat durasi yang sudah berjalan
            print("\n\n⚠️ Timer dihentikan oleh pengguna.")
            waktu_terlewati = (durasi_menit * 60) - detik
            menit_terlewati = waktu_terlewati // 60
            if menit_terlewati >= 1:
                pilihan = input(f"Ingin mencatat {menit_terlewati} menit belajar yang sudah berjalan? (y/n): ").lower()
                if pilihan == 'y':
                    self._proses_log_otomatis(menit_terlewati)
            else:
                print("Sesi terlalu singkat (kurang dari 1 menit) untuk dicatat. Tetap semangat!\n")

    def _proses_log_otomatis(self, menit: int):
        """Helper untuk memandu pembuatan objek sesi belajar setelah Pomodoro."""
        print("\nPilih kategori pembelajaran Anda:")
        print("1. Coding Praktis (SesiCoding)")
        print("2. Belajar Teori / Dokumentasi (SesiMembaca)")
        kategori = input("Pilih (1/2): ")
        
        topik = input("Apa nama topik yang Anda pelajari? : ").strip() or "Belajar Mandiri"
        
        if kategori == '1':
            bahasa = input("Bahasa pemrograman yang digunakan? : ").strip() or "Python"
            try:
                baris = int(input("Perkiraan jumlah baris kode yang ditulis? : ") or "0")
            except ValueError:
                baris = 0
            sesi = SesiCoding(topik, menit, baris, bahasa)
        else:
            sumber = input("Apa sumber bacaan/dokumentasi Anda? : ").strip() or "Dokumentasi Resmi"
            sesi = SesiMembaca(topik, menit, sumber)
            
        self.catat_aktivitas(sesi)


# ==========================================
# 5. MENULIS MENU UTAMA (ENTRY POINT)
# ==========================================
def main():
    tracker = ConsistencyTracker()
    
    while True:
        print("=== MENU UTAMA KONSISTENSI BELAJAR (OOP) ===")
        print("1. Tampilkan Dashboard Stats & Level")
        print("2. Catat Sesi Belajar Manual")
        print("3. Jalankan Pomodoro Timer (Fokus 25 Menit)")
        print("4. Tampilkan Riwayat Aktivitas")
        print("5. Keluar")
        print("============================================")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            tracker.tampilkan_dashboard()
        elif pilihan == '2':
            print("\n--- CATAT SESI MANUAL ---")
            print("Pilih Jenis Aktivitas:")
            print("1. Coding (SesiCoding)")
            print("2. Teori/Membaca (SesiMembaca)")
            jenis = input("Pilihan (1/2): ").strip()
            
            topik = input("Masukkan nama topik: ").strip()
            if not topik:
                print("Topik tidak boleh kosong.")
                continue
                
            try:
                durasi = int(input("Masukkan durasi belajar (menit): ").strip())
            except ValueError:
                print("Durasi harus berupa angka.")
                continue
                
            if jenis == '1':
                bahasa = input("Bahasa pemrograman: ").strip() or "Python"
                try:
                    baris = int(input("Perkiraan baris kode ditulis: ").strip() or "0")
                except ValueError:
                    baris = 0
                sesi = SesiCoding(topik, durasi, baris, bahasa)
            else:
                sumber = input("Sumber bacaan: ").strip() or "Dokumentasi"
                sesi = SesiMembaca(topik, durasi, sumber)
                
            tracker.catat_aktivitas(sesi)
            
        elif pilihan == '3':
            # Sesi pomodoro standar 25 menit
            tracker.jalankan_pomodoro(durasi_menit=25)
        elif pilihan == '4':
            tracker.tampilkan_riwayat()
        elif pilihan == '5':
            print(f"\nSampai jumpa, {tracker.user.nama}! Ingat, konsistensi 15 menit sehari jauh lebih baik daripada 5 jam sekaligus seminggu sekali.")
            print("Keep coding and staying consistent! 🚀\n")
            break
        else:
            print("\nPilihan menu tidak valid. Silakan pilih 1-5.\n")


if __name__ == "__main__":
    main()

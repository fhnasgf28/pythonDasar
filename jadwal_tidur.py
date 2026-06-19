"""
Program Jadwal Tidur
Membantu Anda mengelola jadwal tidur yang sehat
"""

from datetime import datetime, timedelta
import json

class JadwalTidur:
    """Kelas untuk mengelola jadwal tidur"""
    
    def __init__(self, nama):
        self.nama = nama
        self.jadwal = []
        self.durasi_tidur_ideal = 7  # jam
    
    def tambah_jadwal(self, tanggal, jam_mulai, jam_selesai):
        """
        Menambahkan jadwal tidur baru
        
        Args:
            tanggal (str): Format YYYY-MM-DD
            jam_mulai (str): Format HH:MM
            jam_selesai (str): Format HH:MM
        """
        try:
            jadwal_baru = {
                'tanggal': tanggal,
                'jam_mulai': jam_mulai,
                'jam_selesai': jam_selesai,
                'durasi': self.hitung_durasi(jam_mulai, jam_selesai)
            }
            self.jadwal.append(jadwal_baru)
            print(f"✓ Jadwal tidur ditambahkan: {tanggal} ({jadwal_baru['durasi']:.1f} jam)")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def hitung_durasi(self, jam_mulai, jam_selesai):
        """Menghitung durasi tidur dalam jam"""
        try:
            mulai = datetime.strptime(jam_mulai, "%H:%M")
            selesai = datetime.strptime(jam_selesai, "%H:%M")
            
            # Jika selesai lebih kecil dari mulai, anggap besok
            if selesai < mulai:
                selesai += timedelta(days=1)
            
            durasi = (selesai - mulai).total_seconds() / 3600
            return durasi
        except ValueError:
            raise ValueError("Format waktu harus HH:MM")
    
    def tampilkan_jadwal(self):
        """Menampilkan semua jadwal tidur"""
        if not self.jadwal:
            print("Belum ada jadwal tidur")
            return
        
        print(f"\n{'='*60}")
        print(f"JADWAL TIDUR - {self.nama.upper()}")
        print(f"{'='*60}")
        
        total_durasi = 0
        for idx, item in enumerate(self.jadwal, 1):
            print(f"\n{idx}. Tanggal: {item['tanggal']}")
            print(f"   Jam Tidur: {item['jam_mulai']} - {item['jam_selesai']}")
            print(f"   Durasi: {item['durasi']:.1f} jam")
            total_durasi += item['durasi']
        
        rata_rata = total_durasi / len(self.jadwal) if self.jadwal else 0
        print(f"\n{'='*60}")
        print(f"Total Durasi: {total_durasi:.1f} jam")
        print(f"Rata-rata per malam: {rata_rata:.1f} jam")
        print(f"Target ideal: {self.durasi_tidur_ideal} jam")
        print(f"Status: {'✓ Sehat' if rata_rata >= self.durasi_tidur_ideal else '⚠ Kurang Tidur'}")
        print(f"{'='*60}\n")
    
    def analisis_tidur(self):
        """Menganalisis kualitas tidur"""
        if not self.jadwal:
            print("Belum ada data jadwal tidur untuk dianalisis")
            return
        
        durasi_list = [item['durasi'] for item in self.jadwal]
        rata_rata = sum(durasi_list) / len(durasi_list)
        
        print(f"\n{'='*60}")
        print("ANALISIS KUALITAS TIDUR")
        print(f"{'='*60}")
        print(f"Rata-rata tidur: {rata_rata:.1f} jam")
        print(f"Tidur terpanjang: {max(durasi_list):.1f} jam")
        print(f"Tidur terpendek: {min(durasi_list):.1f} jam")
        
        if rata_rata >= 7 and rata_rata <= 9:
            saran = "Pola tidur Anda sudah bagus! Pertahankan rutinitas ini."
        elif rata_rata < 7:
            saran = "Tidur Anda kurang. Cobalah tidur lebih awal atau lama."
        else:
            saran = "Tidur Anda terlalu lama. Coba kurangi durasi tidur."
        
        print(f"Saran: {saran}")
        print(f"{'='*60}\n")
    
    def simpan_ke_file(self, nama_file="jadwal_tidur.json"):
        """Menyimpan jadwal ke file JSON"""
        try:
            data = {
                'nama': self.nama,
                'jadwal': self.jadwal
            }
            with open(nama_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✓ Jadwal disimpan ke {nama_file}")
        except Exception as e:
            print(f"✗ Error menyimpan file: {e}")
    
    def baca_dari_file(self, nama_file="jadwal_tidur.json"):
        """Membaca jadwal dari file JSON"""
        try:
            with open(nama_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.jadwal = data.get('jadwal', [])
            print(f"✓ Jadwal dimuat dari {nama_file}")
        except FileNotFoundError:
            print(f"✗ File {nama_file} tidak ditemukan")
        except Exception as e:
            print(f"✗ Error membaca file: {e}")


def main():
    """Fungsi utama program"""
    print("\n" + "="*60)
    print("PROGRAM JADWAL TIDUR")
    print("="*60 + "\n")
    
    # Membuat instance jadwal tidur
    nama_pengguna = input("Masukkan nama Anda: ").strip() or "Pengguna"
    jadwal = JadwalTidur(nama_pengguna)
    
    while True:
        print("\nPILIHAN MENU:")
        print("1. Tambah jadwal tidur")
        print("2. Lihat jadwal tidur")
        print("3. Analisis kualitas tidur")
        print("4. Simpan jadwal")
        print("5. Baca jadwal dari file")
        print("6. Keluar")
        
        pilihan = input("\nPilih menu (1-6): ").strip()
        
        if pilihan == '1':
            print("\n--- TAMBAH JADWAL TIDUR ---")
            tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
            jam_mulai = input("Jam tidur (HH:MM): ").strip()
            jam_selesai = input("Jam bangun (HH:MM): ").strip()
            jadwal.tambah_jadwal(tanggal, jam_mulai, jam_selesai)
        
        elif pilihan == '2':
            jadwal.tampilkan_jadwal()
        
        elif pilihan == '3':
            jadwal.analisis_tidur()
        
        elif pilihan == '4':
            jadwal.simpan_ke_file()
        
        elif pilihan == '5':
            jadwal.baca_dari_file()
        
        elif pilihan == '6':
            print("\nTerima kasih! Semoga tidur Anda nyenyak! 😴")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()

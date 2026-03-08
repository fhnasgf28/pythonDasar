# Program untuk Menghitung Lama Main Game
# Fitur: tracking waktu, pause/resume, statistik, dll

from datetime import datetime, timedelta
import json
from pathlib import Path

class PelacakWaktuGame:
    """Kelas untuk melacak dan menghitung lama main game"""
    
    def __init__(self, nama_game):
        self.nama_game = nama_game
        self.waktu_mulai = None
        self.waktu_berhenti = None
        self.total_waktu = timedelta(0)
        self.session_list = []
        self.is_playing = False
    
    def mulai_bermain(self):
        """Mulai sesi bermain"""
        if self.is_playing:
            print(f"⚠️  Game '{self.nama_game}' sudah sedang berjalan!")
            return False
        
        self.waktu_mulai = datetime.now()
        self.is_playing = True
        print(f"▶️  Game '{self.nama_game}' dimulai pada {self.waktu_mulai.strftime('%H:%M:%S')}")
        return True
    
    def berhenti_bermain(self):
        """Berhenti bermain dan hitung durasi"""
        if not self.is_playing:
            print(f"⚠️  Game '{self.nama_game}' tidak sedang berjalan!")
            return False
        
        self.waktu_berhenti = datetime.now()
        durasi = self.waktu_berhenti - self.waktu_mulai
        self.total_waktu += durasi
        self.is_playing = False
        
        session = {
            'tanggal': self.waktu_mulai.strftime('%Y-%m-%d'),
            'waktu_mulai': self.waktu_mulai.strftime('%H:%M:%S'),
            'waktu_berhenti': self.waktu_berhenti.strftime('%H:%M:%S'),
            'durasi_detik': int(durasi.total_seconds()),
            'durasi_format': self.format_durasi(durasi)
        }
        self.session_list.append(session)
        
        print(f"⏹️  Game berhenti pada {self.waktu_berhenti.strftime('%H:%M:%S')}")
        print(f"⏱️  Durasi sesi: {session['durasi_format']}")
        return True
    
    @staticmethod
    def format_durasi(durasi):
        """Format durasi dalam format jam:menit:detik"""
        total_detik = int(durasi.total_seconds())
        jam = total_detik // 3600
        menit = (total_detik % 3600) // 60
        detik = total_detik % 60
        return f"{jam:02d}:{menit:02d}:{detik:02d}"
    
    def dapatkan_total_waktu(self):
        """Dapatkan total waktu bermain"""
        return self.total_waktu
    
    def dapatkan_total_waktu_format(self):
        """Dapatkan total waktu dalam format jam:menit:detik"""
        return self.format_durasi(self.total_waktu)
    
    def dapatkan_rata_rata_session(self):
        """Hitung rata-rata durasi per sesi"""
        if not self.session_list:
            return timedelta(0)
        
        total_detik = sum(s['durasi_detik'] for s in self.session_list)
        rata_rata_detik = total_detik // len(self.session_list)
        return timedelta(seconds=rata_rata_detik)
    
    def tampilkan_statistik(self):
        """Tampilkan statistik lengkap bermain game"""
        print("\n" + "="*60)
        print(f"STATISTIK BERMAIN GAME: {self.nama_game}")
        print("="*60)
        
        if not self.session_list:
            print("❌ Belum ada data sesi bermain!")
            return
        
        # Info umum
        print(f"\nℹ️  INFORMASI UMUM:")
        print(f"   Total Sesi Bermain: {len(self.session_list)}")
        print(f"   Total Waktu Bermain: {self.dapatkan_total_waktu_format()}")
        print(f"   Rata-rata per Sesi: {self.format_durasi(self.dapatkan_rata_rata_session())}")
        
        # Detail setiap sesi
        print(f"\n📋 DETAIL SETIAP SESI:")
        print("-"*60)
        for i, session in enumerate(self.session_list, 1):
            print(f"\nSesi {i}:")
            print(f"   Tanggal: {session['tanggal']}")
            print(f"   Mulai: {session['waktu_mulai']} | Berhenti: {session['waktu_berhenti']}")
            print(f"   Durasi: {session['durasi_format']}")
        
        print("\n" + "="*60 + "\n")
    
    def simpan_ke_file(self, filename=None):
        """Simpan data sesi ke file JSON"""
        if filename is None:
            filename = f"{self.nama_game.replace(' ', '_')}_history.json"
        
        data = {
            'nama_game': self.nama_game,
            'total_waktu': str(self.total_waktu),
            'total_sesi': len(self.session_list),
            'session_list': self.session_list
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✓ Data disimpan ke '{filename}'")
            return True
        except Exception as e:
            print(f"❌ Gagal menyimpan: {e}")
            return False
    
    def baca_dari_file(self, filename):
        """Baca data sesi dari file JSON"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.nama_game = data['nama_game']
            self.session_list = data['session_list']
            
            # Hitung ulang total waktu
            total_detik = sum(s['durasi_detik'] for s in self.session_list)
            self.total_waktu = timedelta(seconds=total_detik)
            
            print(f"✓ Data berhasil dimuat dari '{filename}'")
            return True
        except Exception as e:
            print(f"❌ Gagal membaca: {e}")
            return False


# ============================================
# SISTEM PELACAKAN GAME MULTI-GAME
# ============================================

class SistemPelacakGame:
    """Sistem untuk melacak multiple games"""
    
    def __init__(self):
        self.games = {}
    
    def tambah_game(self, nama_game):
        """Tambahkan game baru"""
        if nama_game in self.games:
            print(f"⚠️  Game '{nama_game}' sudah ada!")
            return False
        
        self.games[nama_game] = PelacakWaktuGame(nama_game)
        print(f"✓ Game '{nama_game}' ditambahkan")
        return True
    
    def mulai_game(self, nama_game):
        """Mulai bermain game tertentu"""
        if nama_game not in self.games:
            print(f"❌ Game '{nama_game}' tidak ditemukan!")
            return False
        
        return self.games[nama_game].mulai_bermain()
    
    def berhenti_game(self, nama_game):
        """Berhenti bermain game tertentu"""
        if nama_game not in self.games:
            print(f"❌ Game '{nama_game}' tidak ditemukan!")
            return False
        
        return self.games[nama_game].berhenti_bermain()
    
    def tampilkan_semua_statistik(self):
        """Tampilkan statistik semua game"""
        if not self.games:
            print("❌ Belum ada game yang ditambahkan!")
            return
        
        print("\n" + "="*60)
        print("STATISTIK SEMUA GAME")
        print("="*60)
        
        total_waktu_semua = timedelta(0)
        
        for nama_game, pelacak in self.games.items():
            total_waktu = pelacak.dapatkan_total_waktu()
            total_waktu_semua += total_waktu
            
            if pelacak.session_list:
                print(f"\n📱 {nama_game}")
                print(f"   Sesi: {len(pelacak.session_list)} | Waktu: {pelacak.dapatkan_total_waktu_format()}")
            else:
                print(f"\n📱 {nama_game} - (Belum ada data)")
        
        print(f"\n{'='*60}")
        print(f"Total Waktu Bermain Semua Game: {PelacakWaktuGame.format_durasi(total_waktu_semua)}")
        print("="*60 + "\n")
    
    def tampilkan_peringkat_game(self):
        """Tampilkan game yang paling sering dimainkan"""
        if not self.games:
            print("❌ Belum ada game!")
            return
        
        game_ranking = [(nama, pelacak.dapatkan_total_waktu().total_seconds()) 
                        for nama, pelacak in self.games.items() 
                        if pelacak.session_list]
        
        if not game_ranking:
            print("❌ Belum ada data waktu bermain!")
            return
        
        game_ranking.sort(key=lambda x: x[1], reverse=True)
        
        print("\n" + "="*60)
        print("PERINGKAT GAME BERDASARKAN LAMA BERMAIN")
        print("="*60)
        
        for rank, (nama, waktu_detik) in enumerate(game_ranking, 1):
            durasi = timedelta(seconds=int(waktu_detik))
            print(f"{rank}. {nama:<25} | {PelacakWaktuGame.format_durasi(durasi)}")
        
        print("="*60 + "\n")


# ============================================
# CONTOH PENGGUNAAN 1: SINGLE GAME
# ============================================

def contoh_single_game():
    """Contoh penggunaan untuk satu game"""
    print("\n" + "🎮 "*20)
    print("CONTOH 1: TRACKING SINGLE GAME")
    print("🎮 "*20 + "\n")
    
    # Buat pelacak untuk satu game
    game = PelacakWaktuGame("Dota 2")
    
    # Simulasi bermain
    import time
    
    print("Sesi 1:")
    game.mulai_bermain()
    time.sleep(3)  # Simulasi bermain 3 detik
    game.berhenti_bermain()
    
    time.sleep(1)
    
    print("\nSesi 2:")
    game.mulai_bermain()
    time.sleep(2)  # Simulasi bermain 2 detik
    game.berhenti_bermain()
    
    # Tampilkan statistik
    game.tampilkan_statistik()
    
    # Simpan data
    game.simpan_ke_file()


# ============================================
# CONTOH PENGGUNAAN 2: MULTIPLE GAMES
# ============================================

def contoh_multiple_games():
    """Contoh penggunaan untuk multiple games"""
    print("\n" + "🎮 "*20)
    print("CONTOH 2: TRACKING MULTIPLE GAMES")
    print("🎮 "*20 + "\n")
    
    sistem = SistemPelacakGame()
    
    # Tambahkan games
    games = ["Dota 2", "CS:GO", "Minecraft", "Valorant"]
    for game in games:
        sistem.tambah_game(game)
    
    # Simulasi bermain
    import time
    
    print("\n--- Hari 1 ---")
    sistem.mulai_game("Dota 2")
    time.sleep(2)
    sistem.berhenti_game("Dota 2")
    
    time.sleep(1)
    
    sistem.mulai_game("Minecraft")
    time.sleep(3)
    sistem.berhenti_game("Minecraft")
    
    print("\n--- Hari 2 ---")
    sistem.mulai_game("Valorant")
    time.sleep(2)
    sistem.berhenti_game("Valorant")
    
    sistem.mulai_game("CS:GO")
    time.sleep(1)
    sistem.berhenti_game("CS:GO")
    
    # Tampilkan semua statistik
    sistem.tampilkan_semua_statistik()
    
    # Tampilkan peringkat
    sistem.tampilkan_peringkat_game()


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    # Jalankan contoh
    contoh_single_game()
    contoh_multiple_games()
    
    # Contoh manual
    print("\n" + "="*60)
    print("CONTOH PENGGUNAAN MANUAL")
    print("="*60)
    
    game = PelacakWaktuGame("Elden Ring")
    
    # Simulasi beberapa sesi (dengan durasi yang sudah ditentukan)
    from datetime import timedelta
    
    game.waktu_mulai = datetime.now() - timedelta(hours=1, minutes=30)
    game.waktu_berhenti = datetime.now() - timedelta(hours=0, minutes=30)
    durasi1 = game.waktu_berhenti - game.waktu_mulai
    game.total_waktu += durasi1
    game.session_list.append({
        'tanggal': game.waktu_mulai.strftime('%Y-%m-%d'),
        'waktu_mulai': game.waktu_mulai.strftime('%H:%M:%S'),
        'waktu_berhenti': game.waktu_berhenti.strftime('%H:%M:%S'),
        'durasi_detik': int(durasi1.total_seconds()),
        'durasi_format': game.format_durasi(durasi1)
    })
    
    game.waktu_mulai = datetime.now() - timedelta(hours=0, minutes=45)
    game.waktu_berhenti = datetime.now()
    durasi2 = game.waktu_berhenti - game.waktu_mulai
    game.total_waktu += durasi2
    game.session_list.append({
        'tanggal': game.waktu_mulai.strftime('%Y-%m-%d'),
        'waktu_mulai': game.waktu_mulai.strftime('%H:%M:%S'),
        'waktu_berhenti': game.waktu_berhenti.strftime('%H:%M:%S'),
        'durasi_detik': int(durasi2.total_seconds()),
        'durasi_format': game.format_durasi(durasi2)
    })
    
    game.tampilkan_statistik()

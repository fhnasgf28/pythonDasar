"""
Game Addiction Reducer - Aplikasi untuk Mengurangi Kecanduan Game
Fitur-fitur:
1. Batasan waktu bermain game
2. Sistem reward untuk self-control
3. Tracking aktivitas gaming
4. Rekomendasi kegiatan alternatif
5. Alert dan reminder
"""

import time
import json
from datetime import datetime, timedelta
from pathlib import Path


class GameAddictionReducer:
    def __init__(self, daily_limit_hours=2):
        """
        Inisialisasi Game Addiction Reducer
        
        Args:
            daily_limit_hours (int): Batasan jam bermain game per hari (default 2 jam)
        """
        self.daily_limit_hours = daily_limit_hours
        self.daily_limit_minutes = daily_limit_hours * 60
        self.data_file = "gaming_data.json"
        self.today_date = datetime.now().strftime("%Y-%m-%d")
        self.today_playtime = 0
        self.load_data()
        
    def load_data(self):
        """Load data gaming dari file JSON"""
        if Path(self.data_file).exists():
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                # Reset data jika sudah hari baru
                if data.get("date") != self.today_date:
                    self.today_playtime = 0
                else:
                    self.today_playtime = data.get("playtime_minutes", 0)
        else:
            self.today_playtime = 0
    
    def save_data(self):
        """Simpan data gaming ke file JSON"""
        data = {
            "date": self.today_date,
            "playtime_minutes": self.today_playtime,
            "daily_limit_minutes": self.daily_limit_minutes,
            "timestamp": datetime.now().isoformat()
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_remaining_time(self):
        """Dapatkan sisa waktu bermain game hari ini"""
        remaining = self.daily_limit_minutes - self.today_playtime
        return max(0, remaining)
    
    def can_play(self):
        """Cek apakah masih bisa bermain game"""
        return self.get_remaining_time() > 0
    
    def start_gaming_session(self, game_name="Unknown Game"):
        """
        Mulai sesi gaming dengan alert
        
        Args:
            game_name (str): Nama game yang dimainkan
        """
        if not self.can_play():
            print("❌ TIDAK BISA BERMAIN GAME!")
            print(f"⏰ Anda sudah mencapai batasan harian: {self.daily_limit_hours} jam")
            self.show_alternative_activities()
            return False
        
        remaining_minutes = self.get_remaining_time()
        hours = remaining_minutes // 60
        minutes = remaining_minutes % 60
        
        print(f"\n🎮 Memulai Sesi Gaming: {game_name}")
        print(f"⏱️  Waktu tersisa hari ini: {hours}h {minutes}m")
        print(f"⚠️  Batasan harian: {self.daily_limit_hours} jam")
        print("━" * 50)
        
        return True
    
    def log_playtime(self, minutes):
        """
        Catat waktu bermain game
        
        Args:
            minutes (int): Durasi bermain dalam menit
        """
        self.today_playtime += minutes
        self.save_data()
        
        remaining = self.get_remaining_time()
        
        if remaining <= 0:
            print(f"\n🛑 WAKTU BERMAIN GAME HABIS!")
            print(f"📊 Total waktu bermain hari ini: {self.today_playtime // 60}h {self.today_playtime % 60}m")
            print("💡 Saatnya beristirahat atau melakukan aktivitas lain!")
            self.show_alternative_activities()
        elif remaining <= 30:
            print(f"\n⚠️  PERINGATAN! Waktu bermain tinggal {remaining} menit lagi!")
            print("📝 Segera hentikan sesi gaming dan lakukan aktivitas lain!")
        else:
            print(f"✅ Waktu dicatat. Sisa waktu: {remaining // 60}h {remaining % 60}m")
    
    def take_break_reminder(self, interval_minutes=30):
        """
        Pengingat untuk istirahat
        
        Args:
            interval_minutes (int): Interval pengingat (default 30 menit)
        """
        print(f"\n⏰ PENGINGAT ISTIRAHAT - Istirahat setiap {interval_minutes} menit")
        print("💡 Tips istirahat:")
        print("   • Cuci tangan dan wajah")
        print("   • Minum air putih")
        print("   • Gerakkan badan sebentar")
        print("   • Lihat ke kejauhan (fokus mata)")
        print("   • Ambil napas dalam-dalam")
    
    def show_statistics(self):
        """Tampilkan statistik bermain game"""
        hours = self.today_playtime // 60
        minutes = self.today_playtime % 60
        remaining = self.get_remaining_time()
        remaining_hours = remaining // 60
        remaining_minutes = remaining % 60
        percentage = (self.today_playtime / self.daily_limit_minutes) * 100
        
        print(f"\n📊 STATISTIK GAMING HARI INI ({self.today_date})")
        print("━" * 50)
        print(f"🕐 Waktu bermain: {hours}h {minutes}m")
        print(f"⏳ Sisa waktu: {remaining_hours}h {remaining_minutes}m")
        print(f"📈 Progress: {percentage:.1f}% dari {self.daily_limit_hours} jam")
        
        # Visualisasi progress bar
        bar_length = 30
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"   [{bar}]")
    
    def show_alternative_activities(self):
        """Tampilkan aktivitas alternatif selain bermain game"""
        activities = [
            "📚 Membaca buku atau artikel menarik",
            "🏃 Olahraga (lari, push-up, yoga)",
            "🎨 Menggambar, melukis, atau crafting",
            "🎵 Mendengarkan musik atau podcast",
            "✍️  Menulis jurnal atau blog",
            "🧘 Meditasi atau mindfulness",
            "👥 Berkumpul dengan keluarga/teman",
            "🍽️  Memasak atau mencoba resep baru",
            "🌱 Berkebun atau merawat tanaman",
            "🎸 Belajar musik atau instrumen",
            "💻 Belajar programming atau skill baru",
            "🚶 Jalan-jalan keluar rumah"
        ]
        
        print("\n💡 REKOMENDASI AKTIVITAS ALTERNATIF:")
        print("━" * 50)
        for activity in activities:
            print(f"  {activity}")
    
    def set_daily_limit(self, hours):
        """
        Ubah batasan harian bermain game
        
        Args:
            hours (int): Jam bermain per hari
        """
        self.daily_limit_hours = hours
        self.daily_limit_minutes = hours * 60
        self.save_data()
        print(f"✅ Batasan harian diubah menjadi {hours} jam")
    
    def health_tips(self):
        """Tampilkan tips kesehatan saat bermain game"""
        print("\n💪 TIPS KESEHATAN SAAT BERMAIN GAME:")
        print("━" * 50)
        print("🔍 MATA:")
        print("   • Letakkan layar 50-70cm dari mata")
        print("   • Gunakan filter cahaya biru jika mungkin")
        print("   • Ganti pencahayaan ruangan sesuai kondisi")
        print("   • Istirahat mata setiap 20 menit")
        print("\n🪑 POSTUR TUBUH:")
        print("   • Duduk dengan punggung tegak")
        print("   • Kepala sejajar dengan layar")
        print("   • Lengan membentuk sudut 90 derajat")
        print("   • Kaki menempel di lantai")
        print("\n🧠 MENTAL:")
        print("   • Jangan bermain saat stress atau sedih")
        print("   • Prioritaskan tugas/kewajiban dulu")
        print("   • Cari teman untuk bermain bersama")
        print("   • Tahu kapan harus berhenti")


class GamingGoalsTracker:
    """Tracker untuk mencapai target mengurangi gaming"""
    
    def __init__(self):
        self.goals_file = "gaming_goals.json"
        self.goals = []
        self.load_goals()
    
    def load_goals(self):
        """Load goals dari file"""
        if Path(self.goals_file).exists():
            with open(self.goals_file, 'r') as f:
                self.goals = json.load(f)
    
    def save_goals(self):
        """Simpan goals ke file"""
        with open(self.goals_file, 'w') as f:
            json.dump(self.goals, f, indent=2)
    
    def add_goal(self, goal_name, target_days):
        """
        Tambah goal baru
        
        Args:
            goal_name (str): Nama goal
            target_days (int): Target hari untuk mencapai goal
        """
        goal = {
            "name": goal_name,
            "target_days": target_days,
            "created_date": datetime.now().isoformat(),
            "completed": False
        }
        self.goals.append(goal)
        self.save_goals()
        print(f"✅ Goal '{goal_name}' ditambahkan! Target: {target_days} hari")
    
    def show_goals(self):
        """Tampilkan semua goals"""
        if not self.goals:
            print("📋 Belum ada goals. Tambahkan goal untuk motivasi!")
            return
        
        print("\n🎯 GAMING REDUCTION GOALS:")
        print("━" * 50)
        for i, goal in enumerate(self.goals, 1):
            status = "✅ SELESAI" if goal["completed"] else "⏳ ONGOING"
            print(f"{i}. {goal['name']}")
            print(f"   Target: {goal['target_days']} hari | Status: {status}")


# CONTOH PENGGUNAAN
if __name__ == "__main__":
    print("🎮 GAME ADDICTION REDUCER - Aplikasi Pengurangan Kecanduan Game 🎮")
    print("=" * 60)
    
    # Inisialisasi
    reducer = GameAddictionReducer(daily_limit_hours=2)
    goals_tracker = GamingGoalsTracker()
    
    # Menu Interaktif
    while True:
        print("\n📋 MENU UTAMA:")
        print("━" * 60)
        print("1. Mulai sesi gaming")
        print("2. Catat waktu bermain")
        print("3. Lihat statistik")
        print("4. Lihat aktivitas alternatif")
        print("5. Tips kesehatan")
        print("6. Pengingat istirahat")
        print("7. Tambah goal")
        print("8. Lihat goals")
        print("9. Ubah batasan harian")
        print("0. Keluar")
        print("━" * 60)
        
        choice = input("Pilih menu (0-9): ").strip()
        
        if choice == "1":
            game_name = input("Masukkan nama game: ").strip() or "Unknown Game"
            reducer.start_gaming_session(game_name)
        
        elif choice == "2":
            try:
                minutes = int(input("Berapa menit bermain? "))
                if minutes > 0:
                    reducer.log_playtime(minutes)
                else:
                    print("❌ Masukkan angka positif!")
            except ValueError:
                print("❌ Input tidak valid!")
        
        elif choice == "3":
            reducer.show_statistics()
        
        elif choice == "4":
            reducer.show_alternative_activities()
        
        elif choice == "5":
            reducer.health_tips()
        
        elif choice == "6":
            reducer.take_break_reminder()
        
        elif choice == "7":
            goal_name = input("Nama goal: ").strip()
            try:
                days = int(input("Target hari: "))
                goals_tracker.add_goal(goal_name, days)
            except ValueError:
                print("❌ Input tidak valid!")
        
        elif choice == "8":
            goals_tracker.show_goals()
        
        elif choice == "9":
            try:
                hours = int(input("Batasan harian (jam): "))
                if hours > 0:
                    reducer.set_daily_limit(hours)
                else:
                    print("❌ Masukkan angka positif!")
            except ValueError:
                print("❌ Input tidak valid!")
        
        elif choice == "0":
            print("\n👋 Terima kasih sudah menggunakan Game Addiction Reducer!")
            print("💪 Tetap semangat mengurangi kecanduan game!")
            break
        
        else:
            print("❌ Pilihan tidak valid!")

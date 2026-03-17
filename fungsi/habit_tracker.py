from datetime import datetime, timedelta
from collections import defaultdict
import json

class HabitTracker:
    """Aplikasi untuk menghilangkan kebiasaan buruk dan membangun habit baik"""
    
    def __init__(self):
        self.habits = {}  # Menyimpan data habit
        self.logs = defaultdict(list)  # Menyimpan log aktivitas
    
    def add_habit(self, habit_name, habit_type, goal_days=30):
        """
        Menambah habit baru
        
        Args:
            habit_name (str): Nama habit
            habit_type (str): 'good' untuk habit baik, 'bad' untuk kebiasaan buruk
            goal_days (int): Target hari untuk mencapai habit
        """
        if habit_name in self.habits:
            print(f"❌ Habit '{habit_name}' sudah ada!")
            return False
        
        self.habits[habit_name] = {
            'type': habit_type,
            'goal_days': goal_days,
            'start_date': datetime.now().strftime('%Y-%m-%d'),
            'status': 'active'
        }
        print(f"✅ Habit '{habit_name}' berhasil ditambahkan!")
        return True
    
    def log_habit(self, habit_name, completed=True, notes=""):
        """
        Mencatat progress habit harian
        
        Args:
            habit_name (str): Nama habit
            completed (bool): Apakah habit sudah dikerjakan
            notes (str): Catatan tambahan
        """
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' tidak ditemukan!")
            return False
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        log_entry = {
            'date': today,
            'completed': completed,
            'notes': notes
        }
        
        self.logs[habit_name].append(log_entry)
        status = "✅ SELESAI" if completed else "❌ BELUM"
        print(f"{status} - {habit_name} ({today})")
        return True
    
    def get_streak(self, habit_name):
        """
        Menghitung streak (berapa hari berturut-turut habit dikerjakan)
        """
        if habit_name not in self.logs:
            return 0
        
        logs = sorted(self.logs[habit_name], key=lambda x: x['date'])
        streak = 0
        
        for i in range(len(logs) - 1, -1, -1):
            if logs[i]['completed']:
                streak += 1
            else:
                break
        
        return streak
    
    def get_completion_rate(self, habit_name):
        """
        Menghitung persentase penyelesaian habit
        """
        if habit_name not in self.logs or len(self.logs[habit_name]) == 0:
            return 0
        
        completed = sum(1 for log in self.logs[habit_name] if log['completed'])
        total = len(self.logs[habit_name])
        
        return (completed / total) * 100
    
    def get_habit_analysis(self, habit_name):
        """
        Memberikan analisis detail tentang habit
        """
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' tidak ditemukan!")
            return None
        
        habit_info = self.habits[habit_name]
        completion_rate = self.get_completion_rate(habit_name)
        streak = self.get_streak(habit_name)
        total_logs = len(self.logs[habit_name])
        
        analysis = {
            'habit_name': habit_name,
            'type': habit_info['type'],
            'start_date': habit_info['start_date'],
            'goal_days': habit_info['goal_days'],
            'total_days_tracked': total_logs,
            'completion_rate': f"{completion_rate:.1f}%",
            'current_streak': streak,
            'status': habit_info['status']
        }
        
        return analysis
    
    def display_habit_analysis(self, habit_name):
        """
        Menampilkan analisis habit dengan format yang bagus
        """
        analysis = self.get_habit_analysis(habit_name)
        
        if analysis is None:
            return
        
        print(f"\n{'='*50}")
        print(f"📊 ANALISIS HABIT: {analysis['habit_name'].upper()}")
        print(f"{'='*50}")
        print(f"Tipe          : {analysis['type'].upper()}")
        print(f"Mulai         : {analysis['start_date']}")
        print(f"Target        : {analysis['goal_days']} hari")
        print(f"Hari Tercatat : {analysis['total_days_tracked']} hari")
        print(f"Tingkat Sukses: {analysis['completion_rate']}")
        print(f"Streak Aktual : {analysis['current_streak']} hari berturut-turut")
        print(f"Status        : {analysis['status']}")
        print(f"{'='*50}\n")
    
    def get_recommendations(self):
        """
        Memberikan rekomendasi berdasarkan progress habit
        """
        if not self.habits:
            print("📝 Belum ada habit. Mulai dengan menambahkan habit pertama Anda!")
            return
        
        print(f"\n{'='*50}")
        print("💡 REKOMENDASI UNTUK ANDA")
        print(f"{'='*50}")
        
        for habit_name in self.habits:
            completion_rate = self.get_completion_rate(habit_name)
            streak = self.get_streak(habit_name)
            habit_type = self.habits[habit_name]['type']
            
            if completion_rate == 100:
                print(f"🌟 {habit_name}: Luar biasa! Terus pertahankan momentum ini!")
            elif completion_rate >= 75:
                print(f"💪 {habit_name}: Bagus! Cukup dekat dengan tujuan, jangan menyerah!")
            elif completion_rate >= 50:
                print(f"⚠️  {habit_name}: Mulai meningkat! Tingkatkan konsistensi Anda.")
            else:
                print(f"🚨 {habit_name}: Perlu lebih fokus. Mulai dengan target kecil!")
            
            if habit_type == 'bad' and streak == 0:
                print(f"   → Bagus! Hari ini hindari kebiasaan buruk ini.")
            elif habit_type == 'good' and streak > 0:
                print(f"   → Streak: {streak} hari! Pertahankan momentum.")
        
        print(f"{'='*50}\n")
    
    def show_all_habits(self):
        """
        Menampilkan semua habit yang sedang dijalankan
        """
        if not self.habits:
            print("📝 Belum ada habit yang ditambahkan.")
            return
        
        print(f"\n{'='*50}")
        print("📋 DAFTAR SEMUA HABIT")
        print(f"{'='*50}")
        
        for i, (habit_name, info) in enumerate(self.habits.items(), 1):
            streak = self.get_streak(habit_name)
            completion_rate = self.get_completion_rate(habit_name)
            
            print(f"{i}. {habit_name}")
            print(f"   Tipe: {info['type']} | Mulai: {info['start_date']}")
            print(f"   Streak: {streak} hari | Sukses: {completion_rate:.1f}%")
        
        print(f"{'='*50}\n")


# ===== CONTOH PENGGUNAAN =====
if __name__ == "__main__":
    tracker = HabitTracker()
    
    # Menambah habit baik
    tracker.add_habit("Olahraga Pagi", "good", goal_days=30)
    tracker.add_habit("Baca Buku", "good", goal_days=30)
    tracker.add_habit("Meditasi", "good", goal_days=21)
    
    # Menambah kebiasaan buruk yang ingin dihilangkan
    tracker.add_habit("Makan Junk Food", "bad", goal_days=30)
    tracker.add_habit("Scrolling Media Sosial", "bad", goal_days=30)
    
    print("\n" + "="*50)
    print("🎯 MENCATAT PROGRESS HARIAN")
    print("="*50 + "\n")
    
    # Log habit
    tracker.log_habit("Olahraga Pagi", True, "Lari 5km")
    tracker.log_habit("Baca Buku", True, "Baca 20 halaman")
    tracker.log_habit("Meditasi", True, "Meditasi 10 menit")
    tracker.log_habit("Makan Junk Food", False, "Berhasil hindari!")
    tracker.log_habit("Scrolling Media Sosial", False, "Fokus kerja")
    
    # Log berikutnya
    tracker.log_habit("Olahraga Pagi", True, "Yoga")
    tracker.log_habit("Baca Buku", True, "Lanjut baca")
    tracker.log_habit("Makan Junk Food", False, "Tetap konsisten")
    tracker.log_habit("Scrolling Media Sosial", True, "Istirahat main sosmed")
    
    # Menampilkan semua habit
    tracker.show_all_habits()
    
    # Analisis detail
    tracker.display_habit_analysis("Olahraga Pagi")
    tracker.display_habit_analysis("Makan Junk Food")
    
    # Rekomendasi
    tracker.get_recommendations()

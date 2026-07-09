"""
Anti-PMO Application
Aplikasi untuk membantu mengatasi kecanduan dengan pendekatan OOP Python
Fitur: Tracking, Motivasi, dan Dukungan Kesehatan Mental
"""

from datetime import datetime, timedelta
from enum import Enum
from abc import ABC, abstractmethod
import json


class Status(Enum):
    """Status recovery journey"""
    STRUGGLING = "Sedang Berjuang"
    IMPROVING = "Mulai Membaik"
    STRONG = "Kuat"
    RELAPSE = "Kambuh"


class Motivation:
    """Kelas untuk motivasi dan quotes inspiratif"""
    
    QUOTES = [
        "Setiap hari adalah kesempatan baru untuk menjadi lebih baik.",
        "Kamu lebih kuat dari yang kamu pikir.",
        "Perjalanan seribu mil dimulai dengan satu langkah.",
        "Jangan menyerah sekarang, masa depan cerah menunggu.",
        "Disiplin adalah jembatan antara tujuan dan pencapaian.",
        "Sekali lagi, dengan lebih baik. Tidak pernah terlambat untuk memulai.",
        "Tubuhmu adalah kuil, perlakukan dengan hormat.",
        "Keberhasilan dimulai dengan keputusan untuk mencoba.",
    ]
    
    @staticmethod
    def get_random_motivation():
        """Dapatkan motivasi random"""
        import random
        return random.choice(Motivation.QUOTES)


class HealthTip:
    """Kelas untuk tips kesehatan"""
    
    TIPS = {
        "Olahraga": "Lakukan olahraga ringan 30 menit setiap hari untuk melepas stress.",
        "Meditasi": "Praktik meditasi 10 menit setiap pagi untuk ketenangan pikiran.",
        "Tidur": "Tidur 7-8 jam setiap malam untuk recovery tubuh optimal.",
        "Nutrisi": "Makan makanan sehat dan hindari junk food untuk tubuh yang lebih baik.",
        "Sosial": "Habiskan waktu dengan teman dan keluarga untuk mengurangi isolasi.",
        "Hobi": "Kembangkan hobi positif seperti membaca, menulis, atau seni.",
    }
    
    @staticmethod
    def get_health_tips():
        """Dapatkan semua tips kesehatan"""
        return HealthTip.TIPS


class User:
    """Kelas untuk menyimpan data pengguna"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_at = datetime.now()
        self.status = Status.STRUGGLING
        self.current_streak = 0  # dalam hari
        self.longest_streak = 0
        self.relapse_count = 0
        self.total_days = 0
    
    def update_status(self, new_status):
        """Update status recovery"""
        self.status = new_status
        print(f"✓ Status diperbarui: {new_status.value}")
    
    def get_profile(self):
        """Dapatkan profil pengguna"""
        return {
            "Nama": self.name,
            "Usia": self.age,
            "Status": self.status.value,
            "Streak Saat Ini": f"{self.current_streak} hari",
            "Streak Terpanjang": f"{self.longest_streak} hari",
            "Total Hari Recovery": f"{self.total_days} hari",
            "Jumlah Kambuh": f"{self.relapse_count} kali",
            "Terdaftar Sejak": self.created_at.strftime("%d-%m-%Y %H:%M"),
        }
    
    def __str__(self):
        return f"User: {self.name} ({self.age} tahun) - Status: {self.status.value}"


class Activity(ABC):
    """Abstract class untuk aktivitas positif"""
    
    def __init__(self, name, duration_minutes):
        self.name = name
        self.duration_minutes = duration_minutes
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_benefit(self):
        """Dapatkan manfaat aktivitas"""
        pass


class Exercise(Activity):
    """Kelas untuk olahraga"""
    
    def __init__(self, name, duration_minutes, calories_burned=0):
        super().__init__(name, duration_minutes)
        self.calories_burned = calories_burned
    
    def get_benefit(self):
        return f"Olahraga '{self.name}' selama {self.duration_minutes} menit - Kalori terbakar: {self.calories_burned}"


class Meditation(Activity):
    """Kelas untuk meditasi"""
    
    def __init__(self, name, duration_minutes, focus_type="Umum"):
        super().__init__(name, duration_minutes)
        self.focus_type = focus_type
    
    def get_benefit(self):
        return f"Meditasi '{self.name}' ({self.focus_type}) selama {self.duration_minutes} menit - Pikiran lebih tenang"


class Journal(Activity):
    """Kelas untuk journaling"""
    
    def __init__(self, title, duration_minutes, content):
        super().__init__(title, duration_minutes)
        self.content = content
    
    def get_benefit(self):
        return f"Journal '{self.name}' selama {self.duration_minutes} menit - Ekspresikan perasaan Anda"


class ChallengeTracker:
    """Kelas untuk melacak challenge dan streak"""
    
    def __init__(self):
        self.activities = []
        self.challenges = {
            "7_day": False,
            "30_day": False,
            "90_day": False,
            "100_day": False,
        }
    
    def add_activity(self, activity):
        """Tambah aktivitas positif"""
        self.activities.append(activity)
        print(f"✓ Aktivitas ditambahkan: {activity.name}")
    
    def check_milestone(self, streak_days):
        """Cek milestone yang dicapai"""
        milestones = []
        
        if streak_days >= 7 and not self.challenges["7_day"]:
            self.challenges["7_day"] = True
            milestones.append("🎯 7 Hari - Milestone Pertama!")
        
        if streak_days >= 30 and not self.challenges["30_day"]:
            self.challenges["30_day"] = True
            milestones.append("🏆 30 Hari - Komitmen Bulanan Tercapai!")
        
        if streak_days >= 90 and not self.challenges["90_day"]:
            self.challenges["90_day"] = True
            milestones.append("👑 90 Hari - Transformasi Dimulai!")
        
        if streak_days >= 100 and not self.challenges["100_day"]:
            self.challenges["100_day"] = True
            milestones.append("⭐ 100 Hari - Luar Biasa!")
        
        return milestones
    
    def get_activities_summary(self):
        """Dapatkan ringkasan aktivitas"""
        return {
            "Total Aktivitas": len(self.activities),
            "Aktivitas": [f"- {act.name} ({act.duration_minutes} menit)" for act in self.activities],
            "Milestones Dicapai": self.challenges,
        }


class RecoveryJourney:
    """Kelas utama untuk perjalanan recovery"""
    
    def __init__(self, user):
        self.user = user
        self.tracker = ChallengeTracker()
        self.last_relapse = None
        self.session_logs = []
    
    def log_success_day(self):
        """Catat hari sukses (tidak relapse)"""
        self.user.current_streak += 1
        self.user.total_days += 1
        
        if self.user.current_streak > self.user.longest_streak:
            self.user.longest_streak = self.user.current_streak
        
        self.session_logs.append({
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "type": "success",
            "streak": self.user.current_streak
        })
        
        milestones = self.tracker.check_milestone(self.user.current_streak)
        
        print(f"\n✅ Hari Sukses!")
        print(f"📊 Streak: {self.user.current_streak} hari")
        
        if milestones:
            print("\n🎊 MILESTONE DICAPAI:")
            for milestone in milestones:
                print(f"   {milestone}")
        
        return milestones
    
    def handle_relapse(self, reason=""):
        """Tangani relapse dengan penuh kasih sayang"""
        self.user.relapse_count += 1
        self.last_relapse = datetime.now()
        
        old_streak = self.user.current_streak
        self.user.current_streak = 0
        
        self.session_logs.append({
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "type": "relapse",
            "reason": reason,
            "previous_streak": old_streak
        })
        
        if self.user.total_days > 0:
            self.user.status = Status.RELAPSE
        
        print(f"\n⚠️  Relapse terdeteksi")
        print(f"📝 Alasan: {reason if reason else 'Tidak disebutkan'}")
        print(f"😔 Streak reset dari {old_streak} hari")
        print(f"\n💪 Jangan menyerah! Ini hanya sebuah kesalahan, bukan kegagalan.")
        print(f"🔄 Mari kita mulai lagi dengan lebih kuat.")
    
    def add_positive_activity(self, activity):
        """Tambah aktivitas positif untuk mengalihkan perhatian"""
        self.tracker.add_activity(activity)
        
        if isinstance(activity, Exercise):
            self.user.status = Status.IMPROVING
        
        print(f"💪 Aktivitas positif dicatat!")
    
    def get_motivation(self):
        """Dapatkan motivasi untuk hari ini"""
        quote = Motivation.get_random_motivation()
        print(f"\n💬 Motivasi Hari Ini:")
        print(f"   \"{quote}\"")
        return quote
    
    def get_health_recommendations(self):
        """Dapatkan rekomendasi kesehatan"""
        tips = HealthTip.get_health_tips()
        print("\n🏥 Tips Kesehatan:")
        for category, tip in tips.items():
            print(f"   • {category}: {tip}")
        return tips
    
    def display_dashboard(self):
        """Tampilkan dashboard utama"""
        print("\n" + "="*60)
        print("           🌟 ANTI-PMO RECOVERY DASHBOARD 🌟")
        print("="*60)
        
        profile = self.user.get_profile()
        print("\n👤 PROFIL PENGGUNA:")
        for key, value in profile.items():
            print(f"   {key}: {value}")
        
        print("\n📈 STATISTIK RECOVERY:")
        print(f"   Current Streak: {self.user.current_streak} 🔥")
        print(f"   Longest Streak: {self.user.longest_streak} 💪")
        print(f"   Total Days Clean: {self.user.total_days} 📅")
        print(f"   Relapse Count: {self.user.relapse_count} 📊")
        
        activities = self.tracker.get_activities_summary()
        print(f"\n🏋️  AKTIVITAS POSITIF:")
        print(f"   Total: {activities['Total Aktivitas']}")
        for activity in activities['Aktivitas']:
            print(f"   {activity}")
        
        print("\n" + "="*60 + "\n")
    
    def save_progress(self, filename="progress.json"):
        """Simpan progress ke file"""
        data = {
            "user": {
                "name": self.user.name,
                "age": self.user.age,
                "status": self.user.status.value,
                "current_streak": self.user.current_streak,
                "longest_streak": self.user.longest_streak,
                "total_days": self.user.total_days,
                "relapse_count": self.user.relapse_count,
            },
            "session_logs": self.session_logs,
            "last_saved": datetime.now().strftime("%d-%m-%Y %H:%M"),
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Progress disimpan ke {filename}")


# ==================== DEMO APLIKASI ====================

def main():
    """Fungsi utama untuk demonstrasi"""
    
    print("🚀 Selamat datang di Aplikasi Anti-PMO Recovery!\n")
    
    # Buat user baru
    user = User("Ahmad", 25)
    print(f"✓ User terdaftar: {user}\n")
    
    # Buat recovery journey
    journey = RecoveryJourney(user)
    
    # Tampilkan dashboard awal
    journey.display_dashboard()
    
    # Simulasi aktivitas positif
    print("📋 Menambahkan aktivitas positif...\n")
    
    exercise1 = Exercise("Jogging Pagi", 30, calories_burned=250)
    journey.add_positive_activity(exercise1)
    
    meditation1 = Meditation("Meditasi Pagi", 15, focus_type="Pernapasan")
    journey.add_positive_activity(meditation1)
    
    journal1 = Journal("Refleksi Harian", 20, "Hari ini saya merasa lebih baik...")
    journey.add_positive_activity(journal1)
    
    # Log beberapa hari sukses
    print("\n📅 Mencatat hari-hari sukses...\n")
    for day in range(1, 8):
        print(f"--- Hari ke-{day} ---")
        journey.log_success_day()
        print()
    
    # Tampilkan motivasi
    journey.get_motivation()
    
    # Tampilkan rekomendasi kesehatan
    journey.get_health_recommendations()
    
    # Tampilkan dashboard akhir
    journey.display_dashboard()
    
    # Simulasi relapse dan recovery
    print("\n--- Simulasi Relapse ---")
    journey.handle_relapse("Stress dari pekerjaan")
    
    print("\n--- Kembali ke Track ---")
    for day in range(1, 4):
        print(f"--- Hari Recovery ke-{day} ---")
        journey.log_success_day()
        print()
    
    # Simpan progress
    journey.save_progress()
    
    # Tampilkan dashboard akhir
    journey.display_dashboard()


if __name__ == "__main__":
    main()

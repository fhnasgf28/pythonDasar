from datetime import datetime, timedelta
from collections import defaultdict
import json

class HabitTrackerV1:
    def __init__(self):
        self.habits = {}
        self.logs = defaultdict(list)

        print(f" ini adalah hasil dari logs {self.logs}")
    
    def add_habit(self, habit_name, habit_type, goal_days=30):
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
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' tidak ditemukan!")
            return None
        
        habit_info = self.habits[habit_name]
        completion_rate = self.get_completion_rate(habit_name)
        streak = self.get_streak(habit_name)
        print(f"Habit: {habit_name}")
        total_logs = len(self.logs[habit_name])
        print(f"Total Logs: {total_logs}")

        analysis = {
            'habit_name': habit_name,
            'habit_type': habit_info['type'],
            'goal_days': habit_info['goal_days'],
            'start_date': habit_info['start_date'],
            'status': habit_info['status'],
            'completion_rate': completion_rate,
            'current_streak': streak
        }
        return analysis
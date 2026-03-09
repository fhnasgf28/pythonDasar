import datetime
class HabitTracker:
    def __init__(self, name):
        self.name = name 
        self.history = []
    
    def mark_done(self):
        today = datetime.date.today()
        if today not in self.history:
            self.history.append(today)
            print(f"Habit '{self.name}' marked as done for {today}.")
        else:
            print(f"Habit '{self.name}' is already marked as done for {today}.")

    def get_weekly_progress(self):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=6)
        count = sum(1 for date in self.history if week_ago <= date <= today)
        return count
    
    def __str__(self):
        return f"HabitTracker(name={self.name}, history={self.get_weekly_progress()})"
    

class HabitManager:
    def __init__(self):
        self.habits = {}
    
    def add_habit(self, name):
        if name in self.habits:
            print(f"Habit '{name}' already exists.")
        else:
            self.habits[name] = HabitTracker(name)
            print(f"Habit '{name}' added.")
    
    def mark_done(self, name):
        habit = self.habits.get(name)
        if habit:
            habit.mark_done()
        else:
            print(f"Habit '{name}' not found.")
    
    def show_progress(self):
        print("\nWeekly Progress:")
        for habit in self.habits.values():
            print(f"{habit.name}: {habit.get_weekly_progress()} days done in the last week.")

# simulasi penggunaan
if __name__ == "__main__":
    manager = HabitManager()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Habit")
        print("2. Tandai Habit Selesai")
        print("3. Tampilkan Progress Mingguan")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ")
        
        if choice == '1':
            name = input("Nama habit: ")
            manager.add_habit(name)
        
        elif choice == '2':
            name = input("Nama habit yang ingin ditandai selesai: ")
            manager.mark_done(name)
        
        elif choice == '3':
            manager.show_progress()
        
        elif choice == '4':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
# Habit Tracker Program
# This program allows users to track their habits, mark them as done, and view their weekly progress.
# It includes classes for managing habits and tracking their completion history.
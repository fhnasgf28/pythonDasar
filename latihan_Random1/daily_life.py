import time 

class Task:
    def __init__(self, name, energy_cost):
        self.name = name 
        self.energy_cost = energy_cost
        self.is_completed = False
    
    def complete(self):
        self.is_completed = True
        print(f"Task '{self.name}' completed!")

class Developer:
    def __init__(self, name, energy=100):
        self.name = name 
        self.energy = energy
        self.daily_tasks = []

    def drink_coffee(self):
        self.energy += 30 
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} drinks coffee. Energy is now {self.energy}.")
    
    def add_task(self, task):
        self.daily_tasks.append(task)
        print(f"📝 Agenda ditambahkan: {task.name} (Butuh energi: {task.energy_cost}%)")
    
    def work(self):
        print(f"\n{self.name} mulai bekerja...")
        for task in self.daily_tasks:
            if task.is_completed:
                continue
            if self.energy >= task.energy_cost:
                print(f"🔨 Mengerjakan: {task.name} (Butuh energi: {task.energy_cost}%)")
                time.sleep(1)  # Simulasi waktu kerja
                self.energy -= task.energy_cost
                task.complete()
                print(f"⚡ Energi tersisa: {self.energy}%")
            else:
                print(f"⚠️ Energi tidak cukup untuk mengerjakan '{task.name}'. Pertimbangkan untuk minum kopi.")
                break
    
    def sleep(self):
        self.energy = 100
        for task in self.daily_tasks:
            task.is_completed = False
        print(f"{self.name} tidur dan pulih. Energi kembali ke {self.energy}%.")

# IMPLEMENTASI KEHIDUPAN SEHARI HARI 
if __name__ == "__main__":
    dev = Developer("Alice")
    
    # Menambahkan tugas harian
    dev.add_task(Task("Menyelesaikan laporan", 40))
    dev.add_task(Task("Meeting dengan tim", 30))
    dev.add_task(Task("Coding fitur baru", 50))
    
    # Mulai bekerja
    dev.work()
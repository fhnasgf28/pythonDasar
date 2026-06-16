class Task:
    def __init__(self, name, energy_cost, is_urgent=False):
        self.name = name 
        self.energy_cost = energy_cost 
        self.is_completed = False
        self.is_urgent = is_urgent
    
    def complete(self):
        self.is_completed = True
        print(f"Task '{self.name}' completed!")

class Developer:
    def __init__(self, name, energy=100):
        self.name = name 
        self.energy = energy
        self.daily_tasks = []
    
    def add_task(self, task):
        self.daily_tasks.append(task)
        status = "URGENT" if task.is_urgent else "Normal"
        print(f"📝 Agenda ditambahkan: {task.name} (Butuh energi: {task.energy_cost}%) - {status}")
    
    def work_urgent_only(self):
        print(f"\n{self.name} mode panik! Hanya mengerjakan tugas URGENT...")
        for task in self.daily_tasks:
            if task.is_completed:
                continue
            if task.is_urgent:
                if self.energy >= task.energy_cost:
                    print(f"Developer {self.name} mengerjakan: {task.name} (Butuh energi: {task.energy_cost}%)")
                    self.energy -= task.energy_cost
                    task.complete()
                    print(f"⚡ Energi tersisa: {self.energy}%")
                else:
                    print(f"⚠️ Energi tidak cukup untuk mengerjakan '{task.name}'. Pertimbangkan untuk minum kopi.")
                    break
            else:
                print(f"⚠️ Tugas '{task.name}' tidak urgent, dilewati dulu.")

if __name__ == "__main__":
    dev = Developer("Bob")
    
    # Menambahkan tugas harian
    dev.add_task(Task("Menyelesaikan laporan", 40))
    dev.add_task(Task("Meeting dengan tim", 30, is_urgent=True))
    dev.add_task(Task("Coding fitur baru", 50))
    
    # Mulai bekerja dengan mode panik (hanya mengerjakan tugas urgent)
    dev.work_urgent_only()
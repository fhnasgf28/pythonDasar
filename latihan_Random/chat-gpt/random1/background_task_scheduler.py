import time
import threading
from typing import Callable

class Task:
    def __init__(self, name:str, func:Callable, interval:int):
        self.name = name
        self.func = func
        self.interval = interval
        self.last_run = 0
    
    def should_run(self):
        return time.time() - self.last_run >= self.interval
    
    def run(self):
        print(f"Running task: {self.name}")
        self.func()
        self.last_run = time.time()

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        print(f"[Scheduler] Adding task: {task.name} add with interval {task.interval} seconds")
        self.tasks.append(task)
    
    def start(self):
        print("[scheduler] Starting scheduler...")
        try:
            while True:
                for task in self.tasks:
                    if task.should_run():
                        threading.Thread(target=task.run).start()
                    time.sleep(1)  # Sleep to prevent busy waiting
        except KeyboardInterrupt:
            print("[scheduler] Stopping scheduler...")
            self.stop()


# contoh fungsi yang akan dijalankan
def print_hello():
    print("Hello, world!")

def print_time():
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")


def show_reminder():
    print("Don't forget to take a break and stretch!")

# main sheduler 
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Menambahkan tugas ke scheduler
    scheduler.add_task(Task("Print Hello", print_hello, 5))  # Setiap 5 detik
    scheduler.add_task(Task("Print Time", print_time, 10))   # Setiap 10 detik
    scheduler.add_task(Task("Show Reminder", show_reminder, 15))  # Setiap 15 detik
    
    # Memulai scheduler
    scheduler.start()
    

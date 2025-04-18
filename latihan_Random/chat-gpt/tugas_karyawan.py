from datetime import date

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.status = "To Do"

    def update_status(self, new_status):
        if new_status in ["To Do", "In Progress", "Done"]:
            self.status = new_status
        else:
            raise ValueError("Invalid status")

    def __str__(self):
        return f"{self.name} ({self.deadline}, {self.status})"

class Employee:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print(f"Tugas untuk {self.name}:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def update_task_status(self, task_index, new_status):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].update_status(new_status)
        else:
            raise ValueError("Invalid task index")

def main():
    emp1 = Employee("John")
    emp2 = Employee("Jane")

    task1 = Task("Buat laporan mingguan", date(2023, 5, 1))
    task2 = Task("Buat laporan bulanan", date(2023, 5, 2))
    task3 = Task("Buat laporan tahunan", date(2023, 5, 3))

    emp1.assign_task(task1)
    emp1.assign_task(task2)
    emp2.assign_task(task3)

    emp1.show_tasks()
    emp2.show_tasks()

    emp1.update_task_status(0, "In Progress")
    emp2.update_task_status(0, "Done")

    emp1.show_tasks()
    emp2.show_tasks()

if __name__ == "__main__":
    main()

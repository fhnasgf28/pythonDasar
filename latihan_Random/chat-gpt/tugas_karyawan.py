from datetime import date

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.status = "To Do"

    def is_overdue(self):
        return self.deadline < date.today() and self.status != "Done"

    def update_status(self, new_status):
        if new_status in ["To Do", "In Progress", "Done"]:
            self.status = new_status
        else:
            raise ValueError("Invalid status")

    def __str__(self):
        overdue_mark = " (Overdue)" if self.is_overdue() else ""
        return f"{self.name} ({self.deadline}, {self.status}) {overdue_mark}"

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

    def show_overdue_tasks(self):
        print(f"Overdue tasks for {self.name}:")
        overdue = [t for t in self.tasks if t.is_overdue()]
        if overdue:
            for task in overdue:
                print(task)
        else:
            print("No overdue tasks.")

    def filter_tasks_by_status(self, status):
        print(f"Tasks for {self.name} with status '{status}':")
        filtered = [t for t in self.tasks if t.status == status]
        if filtered:
            for task in filtered:
                print(task)
        else:
            print("No tasks with the specified status.")

def main():
    emp1 = Employee("John")
    emp2 = Employee("Jane")

    task1 = Task("Buat laporan mingguan", date(2023, 5, 1))
    task2 = Task("Buat laporan bulanan", date(2023, 5, 2))
    task3 = Task("Buat laporan tahunan", date(2023, 5, 3))
    terlambat = Task("Buat laporan tahunan", date(2022, 5, 3))

    emp1.assign_task(terlambat)

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

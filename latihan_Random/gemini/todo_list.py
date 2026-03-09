class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"[{'✓' if self.completed else ' '}] {self.title} (Deadline: {self.deadline})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline):
        task = Task(title, deadline)
        self.tasks.append(task)

    def view_task(self, title, deadline):
        task = Task(title, deadline)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
        else:
            print("Index tugas tidak valid")

# membuat objek todolist
todo_list = TodoList()

# menambahkan beberapa tugas
todo_list.add_task("Belajar Python", "2023-12-31")
todo_list.add_task("Selesaikan Proyek","2023-12-25")
# menampilkan semua tugas
todo_list.view_tasks()

# menandai tugas pertama sebagai selesai
todo_list.mark_task_complete(0)

# menampilkan kembali semua tugas
todo_list.view_tasks()
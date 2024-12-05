class Task:
    task_counter = 0

    def __init__(self, title):
        self.id = Task.task_counter
        self.title = title
        self.completed = False
        Task.task_counter += 1

class TodoList:
    def __init__(self):
        self.tasks= []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"Task {new_task.id} added: {new_task.title}")
        print(f"Task '{title}' added to the list.")

    def remove_task(self, task_id):
        task_found = False
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f'Task {task.title} removed from the list.')
                task_found = True
                break
        if not task_found:
            print(f"Task with ID {task_id} not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task.completed else "Not Completed"
                print(f"Task {task.id}: {task.title} ({status})")

# example usage
todo_list = TodoList()
todo_list.add_task("Task 1")
todo_list.add_task("Task 2")
todo_list.add_task("Task 3")
todo_list.remove_task(1)
todo_list.display_tasks()
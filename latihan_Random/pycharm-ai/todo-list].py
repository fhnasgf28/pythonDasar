import json
class Task:
    task_counter = 0

    def __init__(self, title, task_id=None, completed=False):
        self.id = task_id if task_id is not None else Task.task_counter
        self.title = title
        self.completed = completed
        Task.task_counter = max(Task.task_counter, self.id + 1)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

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

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            tasks_list = [task.to_dict() for task in self.tasks]
            json.dump(tasks_list, file, indent=4)
        print(f"Todo list saved to {filename}")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_list = json.load(file)
                self.tasks = [Task(task['title'], task['id'], task['completed']) for task in tasks_list]
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Invalid JSON data in {filename}.")
            print(f"Todo list loaded from {filename}")

# example usage
todo_list = TodoList()
todo_list.add_task("Task 1")
todo_list.add_task("Task 2")
todo_list.add_task("Task 3")
todo_list.remove_task(1)
todo_list.display_tasks()

# save to JSON
todo_list.save_to_json("todo_list.json")

# load from JSON
todo_list = TodoList()
todo_list.load_from_json("todo_list.json")
todo_list.display_tasks()
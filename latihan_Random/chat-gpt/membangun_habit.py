import os

TODO_file = "todo_list.txt"

def load_tasks():
    if os.path.exists(TODO_file):
        with open(TODO_file, 'r') as file:
            return [task.strip() for task in file.readlines()]

    return

def save_tasks(tasks):
    with open(TODO_file, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)
import os

TODO_file = "todo_list.txt"

def load_tasks():
    if os.path.exists(TODO_file):
        with open(TODO_file, 'r') as file:
            return [task.strip() for task in file.readlines()]

    return []

def save_tasks(tasks):
    with open(TODO_file, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)
def show_tasks():
    """Menampilkan semua tugas."""
    tasks = load_tasks()
    if not tasks:
        print("Tidak ada tugas dalam daftar.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"tugas '{task}' telah ditambahkan")

def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Tugas '{removed_task}' telah dihapus!")
    else:
        print("Nomor tugas tidak valid.")

def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            task = input("Masukkan tugas: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_tasks()
            try:
                task_num = int(input("Masukkan nomor tugas yang akan dihapus: "))
                delete_task(task_num)
            except ValueError:
                print("Masukkan angka yang valid!")
        elif choice == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
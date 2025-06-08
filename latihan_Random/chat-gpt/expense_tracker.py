import csv
import os

EXPENSE_FILE = "expense.csv"

def load_expenses():
    """Membaca pengeluaran dari file csv"""
    if not os.path.exists(EXPENSE_FILE):
        return []

    with open(EXPENSE_FILE, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

def add_expense(date, category, amount):
    expenses = load_expenses()
    expenses.append([date, category,amount])
    save_expenses(expenses)
    print(f'ini adalah {expenses}')
    print(f"Pengeluaran '{category}' sebesar {amount} telah ditambahkan")

def show_expenses():
    """Menampilkan semua pengeluaran"""
    expenses = load_expenses()
    if not expenses:
        print("Belum ada pengeluaran")
        return

    print("\n Daftar pengeluaran:")
    print("{:<12} {:<15} {:<10}".format("Tanggal", "Kategori", "Jumlah"))
    print("-" * 40)
    for date, category, amount in expenses:
        print(f"{date:<12} {category:<15} {amount:<10}")

def total_expense_by_category():
    """Menghitung total pengeluaran berdasarkan kategory"""
    expenses = load_expenses()
    category_totals = {}

    for _, category, amount in expenses:
        amount = float(amount)
        category_totals[category] = category_totals.get(category, 0) + amount
        print(f'ini adalah kategory {category_totals}')

    print("\nTotal pengeluaran per kategory: ")
    for category, total in  category_totals.items():
        print(f"{category}: {total}")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total per Kategori")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            category = input("Masukkan kategori (makan, transport, dll.): ")
            amount = input("Masukkan jumlah pengeluaran: ")
            add_expense(date, category, amount)
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expense_by_category()
        elif choice == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

# main.py
from income import Income
from expenses import Expenses
from report import Report

def main():
    income = Income()
    expenses = Expenses()

    while True:
        print("\n=== Financial Manager ===")
        print("1. Tambah Pendapatan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Laporan")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            source = input("Sumber Pendapatan: ")
            amount = float(input("Jumlah Pendapatan: "))
            income.add_income(source, amount)
            print(f"Pendapatan dari {source} sebesar Rp{amount:,} ditambahkan!")

        elif choice == "2":
            category = input("Kategori Pengeluaran: ")
            amount = float(input("Jumlah Pengeluaran: "))
            expenses.add_expense(category, amount)
            print(f"Pengeluaran untuk {category} sebesar Rp{amount:,} ditambahkan!")

        elif choice == "3":
            report = Report(income, expenses)
            print(report.generate_report())

        elif choice == "4":
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

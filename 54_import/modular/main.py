import tax_calculator
import expense_tracker


def main():
    while True:
        print("\n=== APLIKASI KEUANGAN ===")
        print("1. Hitung Pajak Penghasilan")
        print("2. Tambah Pengeluaran Harian")
        print("3. Lihat Pengeluaran")
        print("4. Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            income = float(input("Masukkan pendapatan: "))
            tax = tax_calculator.calculator_tax(income)
            print(f"pajak yang harus dibayar: {tax:,.2f}")
        elif choice == "2":
            amount = float(input("Masukkan jumlah pengeluaran: "))
            category = input("Masukkan kategori pengeluaran: ")
            expense_tracker.add_expense(amount, category)
        elif choice == "3":
            expense_tracker.view_expenses()
        elif choice == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
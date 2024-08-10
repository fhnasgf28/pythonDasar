class Transaction:
    def __init__(self, date, description, amount, type1):
        self.date = date
        self.description = description
        self.amount = amount
        self.type = type


transactions = []


def add_transaction():
    date = input('Masukkan tanggal (YYYY-MM-DD):')
    description = input("Masukkan deskripsi:")
    amount = float(input("Masukan jumlah :"))
    type1 = input("Jenis transaksi (expense/income) :")

    transaction = Transaction(date, description, amount, type1)
    transactions.append(transaction)
    print("Transaksi berhasil di tambahkan!")


def view_transactions():
    if not transactions:
        print("Belum ada transaksi")
        return

    print("Daftar Transaksi:")
    for transaction in transactions:
        print(f"{transaction.date} - {transaction.description}: {transaction.amount:.2f} ({transaction.type})")

def generate_report():
    if not transactions:
        print("Belum ada transaksi.")
        return

    total_expense = 0
    total_income = 0
    for transaction in transactions:
        if transaction.type == 'expense':
            total_expense += transaction.amount
        else:
            total_income += transaction.amount
    net_balance = total_income - total_expense

    print("\nLaporan Keuangan:")
    print(f"Pendapatan: {total_income:.2f}")
    print(f"Pengeluaran: {total_expense:.2f}")
    print(f"Saldo Bersih: {net_balance:.2f}")


def main_menu():
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Hasilkan Laporan")
        print("4. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
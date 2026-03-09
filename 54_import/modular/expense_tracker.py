import datetime

expenses = []

def add_expense(amount, category):
    date = datetime.date.today().strftime("%Y-%m-%d")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })
    print(f"Pengeluaran Rp {amount:,.2f} untuk {category} telah dicatat.")

def view_expenses():
    print("Daftar Pengeluaran:")
    if not expenses:
        print('Belum ada pengeluaran')
        return

    total = 0
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: {expense['amount']:,.2f}")
        total += expense['amount']
    print(f"Total Pengeluaran: {total:,.2f}")

if __name__ == "__main__":
    add_expense(10000, "Makanan")
    add_expense(5000, "Transportasi")
    view_expenses()
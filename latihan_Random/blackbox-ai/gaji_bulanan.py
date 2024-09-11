salary = 4500000

expenses = {
    'rent': 1500000,
    'food': 1000000,
    'transportation': 500000,
    'entertainment': 200000,
    'others': 200000
}

total_expenses = sum(expenses.values())
remaining_balance = salary - total_expenses

print('Monthly Expenses: ')
for item, amount in expenses.items():
    print(f"{item.capitalize()}: {amount: ,}")

print(f"Total Expenses: {total_expenses:,}")
print(f"Remaining Balance: {remaining_balance:,}")
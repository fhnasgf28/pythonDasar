class Expenses:
    def __init__(self):
        self.records = []

    def add_expense(self, category, amount):
        self.records.append({
            "category": category,
            "amount": amount
        })

    def get_total_expenses(self):
        return sum(expense["amount"] for expense in self.records)

    def show_expenses(self):
        return self.records
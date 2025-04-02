from income import Income
from expenses import Expenses

class Report:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def generate_report(self):
        total_income = self.income.get_total_income()
        total_expenses = self.expenses.get_total_expenses()
        tax = self.income.calculate_tax()
        balance = total_income - (total_expenses + tax)

        report = f"========= Financial Report =========\n"
        report += f"Total Income: {total_income:,}\n"
        report += f"Total Expenses: {total_expenses:,}\n"
        report += f"Tax: {tax:,}\n"
        report += f"Balance: {balance:,}\n"
        return report
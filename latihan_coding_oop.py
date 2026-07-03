import sys
from typing import Dict

class ExpenseItem:
    """Represents a single expense item with a name and cost."""
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

class BudgetManager:
    """Manages monthly salary and list of expenses using OOP approach."""
    def __init__(self, monthly_salary: int):
        self.monthly_salary = monthly_salary
        self._expenses: Dict[str, int] = {}

    def add_expense(self, name: str, cost: int) -> None:
        """Adds or updates an expense item."""
        if cost < 0:
            raise ValueError("Expense cost cannot be negative.")
        self._expenses[name] = cost

    @property
    def total_expense(self) -> int:
        """Calculates total expenses."""
        return sum(self._expenses.values())

    @property
    def remaining_salary(self) -> int:
        """Calculates remaining salary."""
        return self.monthly_salary - self.total_expense

    def get_financial_status(self) -> str:
        """Determines the status of the budget."""
        remaining = self.remaining_salary
        if remaining > 0:
            return "Keuangan masih aman, masih ada sisa gaji."
        elif remaining == 0:
            return "Gaji habis pas untuk kebutuhan bulanan."
        else:
            return "Pengeluaran melebihi gaji, perlu mengurangi belanja."

    def print_simulation_report(self) -> None:
        """Prints a well-formatted monthly budget simulation report."""
        print("=== SIMULASI BELANJA BULANAN (OOP) ===")
        print(f"Gaji bulanan      : Rp {self.monthly_salary:,}")
        print("\nRincian Kebutuhan:")
        for idx, (item, cost) in enumerate(self._expenses.items(), 1):
            print(f"  {idx}. {item.capitalize():<15}: Rp {cost:,}")
        print("-" * 38)
        print(f"Total belanja     : Rp {self.total_expense:,}")
        print(f"Sisa gaji         : Rp {self.remaining_salary:,}")
        print(f"Status Keuangan   : {self.get_financial_status()}")
        print("======================================")

# Running the simulation
if __name__ == "__main__":
    # Initialize with 5 million salary
    manager = BudgetManager(monthly_salary=5_000_000)

    # Add standard monthly needs
    manager.add_expense("beras", 150_000)
    manager.add_expense("minyak", 80_000)
    manager.add_expense("gula", 50_000)
    manager.add_expense("telur", 120_000)
    manager.add_expense("sayur", 100_000)
    manager.add_expense("daging", 200_000)
    manager.add_expense("susu", 90_000)
    manager.add_expense("sabun", 40_000)
    manager.add_expense("listrik", 300_000)
    manager.add_expense("air", 100_000)
    manager.add_expense("internet", 250_000)

    # Print the report
    manager.print_simulation_report()

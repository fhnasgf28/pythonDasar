class Income:
    def __init__(self):
        self.sources = {}

    def add_income(self, source, amount):
        if source in self.sources:
            self.sources[source] += amount
        else:
            self.sources[source] = amount

    def calculate_tax(self):
        total_income = sum(self.sources.values())
        if total_income <= 50000000:
            tax = total_income * 0.05
        elif total_income <= 250000000:
            tax = total_income * 0.15
        else:
            tax = total_income * 0.25
        return tax

    def get_total_income(self):
        return sum(self.sources.values())

    def show_income(self):
        return self.sources
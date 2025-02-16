class Purchase:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - {self.category} - Rp {self.price} x {self.quantity} = Rp{self.get_total_price()}"
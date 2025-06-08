from datetime import datetime

class Transaction:
    def __init__(self, customer):
        self.customer = customer
        self.item = []
        self.date = datetime.now()

    def add_product(self, product, quantity):
        self.item.append((product, quantity))

    def total(self):
        return sum(product.price * quantity for product, quantity in self.item)
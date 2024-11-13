import json
from datetime import datetime


# kelas untuk mewakili barang yang bisa di beli atau dijual
class Item:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            print(f"Stok tidak cukup untuk {self.name}")
            return False
        self.stock -= quantity
        return True

# kelas transaction untuk menyimpan informasi transaksi
class Transaction:
    def __init__(self, item, quantity, transaction_type):
        self.item = item
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
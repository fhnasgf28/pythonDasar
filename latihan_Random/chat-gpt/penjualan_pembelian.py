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
        self.total_price = item.price * quantity

# kelas store untuk mengelola barang, transaksi dan biaya operasional
class Store:
    def __init__(self, name, montly_operational_cost):
        self.name = name
        self.montly_operational_cost = montly_operational_cost
        self.items = {}
        self.transactions = []

    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = item
        else:
            print(f"Item {item.name} sudah ada di toko.")

    def buy_item(self, item_name, quantity):
        item = self.items.get(item_name)
        if not item:
            print(f"Item {item_name} tidak ada di toko.")
            return

        item.add_stock(quantity)
        transaction = Transaction(item, quantity, "Pembelian")
        self.transactions.append(transaction)
        print(f"Item {item_name} berhasil dibeli sebanyak {quantity} buah.")

    def sell_item(self, item_name, quantity):
        item = self.items.get(item_name)
        if not item:
            print(f"Item {item_name} tidak ditemukan")
            return

        if item.reduce_stock(quantity):
            transaction = Transaction(item, quantity, "Penjualan")
            self.transactions.append(transaction)
            print(f"Item {item_name} berhasil dijual sebanyak {quantity} buah.")

    def calculate_monthly_income(self):
        total_income = sum(t.total_price for t in self.transactions if t.transaction_type == "Penjualan")
        total_expense = sum(t.total_price for t in self.transactions if t.transaction_type == "Pembelian")
        net_profit = total_income - (total_expense + self.montly_operational_cost)

        report = {
            "store_name": self.name,
            "monthly_income": total_income,
            "monthly_expense": total_expense,
            "operational_cost": self.montly_operational_cost,
            "net_profit": net_profit,
            "transactions": [
                {
                    "date": t.date,
                    "item": t.item.name,
                    "quantity": t.quantity,
                    "type": t.transaction_type,
                    "total_price": t.total_price
                } for t in self.transactions
            ]
        }
        return report

    def export_report_to_json(self, filename):
        report = self.calculate_monthly_income()
        with open(filename, 'w') as file:
            json.dump(report, file, indent=4)
        print(f"Laporan bulanan disimpan ke {filename}")


# Simulasi
if __name__ == "__main__":
    # Inisialisasi toko
    store = Store("Toko Serba Ada", montly_operational_cost=2000)

    # Menambahkan item ke inventaris
    item1 = Item("Laptop", 5000, 10)
    item2 = Item("Smartphone", 3000, 20)

    store.add_item(item1)
    store.add_item(item2)

    # Melakukan pembelian dan penjualan
    store.buy_item("Laptop", 5)
    store.sell_item("Smartphone", 3)
    store.sell_item("Laptop", 2)

    # Menghitung laporan bulanan dan ekspor ke JSON
    store.export_report_to_json("monthly_report.json")




import json
from datetime import datetime


# kelas untuk mendefinisikan buah
class Fruit:
    def __init__(self, name, price_per_kg):
        self.name = name
        self.price_per_kg = price_per_kg

    def __repr__(self):
        return f'{self.name} - ${self.price_per_kg}/kg'

    # kelas untuk mencatat transaksi penjualan buah


class SalesRecord:
    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = quantity
        self.total = self.calculate_total()
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def calculate_total(self):
        return self.fruit.price_per_kg * self.quantity

    def to_dict(self):
        return {
            "fruit": self.fruit.name,
            "quantity": self.quantity,
            "total": self.total,
            "date": self.date
        }


# class untuk mengelola penjualan dan menyimpan dalam file JSON
class SalesManager:
    def __init__(self, sales_file='sales_data.json'):
        self.sales_file = sales_file
        self.load_sales()

    def load_sales(self):
        try:
            with open(self.sales_file, 'r') as file:
                content = file.read().strip()
                self.sales_data = json.load(content) if content else []
        except (FileNotFoundError, json.JSONDecodeError):
            self.sales_data = []

    def record_sale(self, sale):
        self.sales_data.append(sale.to_dict())
        self.save_sales()

    def save_sales(self):
        with open(self.sales_file, 'w') as file:
            json.dump(self.sales_file,file, indent=4)

    def calculate_total_revenue(self):
        return sum(sale['total'] for sale in self.sales_data)

    def show_sales(self):
        for sale in self.sales_data:
            print(sale)

# Contoh penggunaan
if __name__ == "__main__":
    # Buat buah
    apple = Fruit("Apple", 3.5)  # Harga per kg dalam USD
    banana = Fruit("Banana", 2.0)

    # Buat manager penjualan
    manager = SalesManager()

    # Buat transaksi penjualan
    sale1 = SalesRecord(apple, 5)  # Menjual 5 kg apel
    sale2 = SalesRecord(banana, 8) # Menjual 8 kg pisang

    # Simpan penjualan ke file JSON
    manager.record_sale(sale1)
    manager.record_sale(sale2)

    # Tampilkan semua penjualan
    print("Daftar Penjualan:")
    manager.show_sales()

    # Hitung total pendapatan
    print("\nTotal Pendapatan:", manager.calculate_total_revenue())
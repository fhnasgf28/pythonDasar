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

class PurchaseManager:
    def __init__(self):
        self.purchases = []

    def add_purchase(self, name, category, price, quantity):
        purchase = Purchase(name, category, price, quantity)
        self.purchases.append(purchase)

    def show_all_purchases(self):
        if not self.purchases:
            print("No purchases found.")
        else:
            for purchase in self.purchases:
                print(purchase)

    def search_by_category(self, category):
        result = [p for p in self.purchases if p.category.lower() == category.lower()]
        print('result farhan28:', result)
        return result if result else "No purchases found for the specified category."

    def search_by_price_range(self, min_price, max_price):
        result = [p for p in self.purchases if min_price <= p.price <= max_price]
        print('result farhan:', result)
        return result if result else "No purchases found within the specified price range."

    def get_total_spent(self):
        return sum(p.get_total_price() for p in self.purchases)

# ==============================
# LATIHAN: COBA JALANKAN KODE INI!
# ==============================

if __name__ == "__main__":
    manager = PurchaseManager()

    # TODO: Tambahkan beberapa data pembelian elektronik
    manager.add_purchase("Laptop Asus", "Laptop", 15000000, 1)
    manager.add_purchase("Headphone Sony", "Aksesoris", 750000, 2)
    manager.add_purchase("Monitor LG", "Monitor", 3000000, 1)

    # TODO: Tampilkan semua pembelian
    print("\n=== Daftar Pembelian ===")
    manager.show_all_purchases()

    # TODO: Cari barang berdasarkan kategori
    print("\n=== Cari Berdasarkan Kategori: Laptop ===")
    result = manager.search_by_category("Laptop")
    for item in result if isinstance(result, list) else [result]:
        print(item)

    # TODO: Cari barang berdasarkan rentang harga
    print("\n=== Cari Berdasarkan Rentang Harga: 1jt - 5jt ===")
    result = manager.search_by_price_range(1000000, 5000000)
    for item in result if isinstance(result, list) else [result]:
        print(item)

    # TODO: Tampilkan total pengeluaran
    print("\n=== Total Pengeluaran ===")
    print(f"Rp{manager.get_total_spent()}")
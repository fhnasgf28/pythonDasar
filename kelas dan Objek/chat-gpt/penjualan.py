# Studi Kasus:
# Anda diminta untuk membuat sebuah sistem sederhana
# untuk mengelola penjualan di sebuah toko. Toko ini menjual
# beberapa produk dan mencatat transaksi penjualan. Setiap transaksi
# penjualan mencatat produk yang dijual, jumlahnya, dan harga per unit saat transaksi dilakukan.
#
# Sistem harus mendukung fitur berikut:
#
# Menambahkan produk baru ke dalam katalog produk.
# Menambahkan transaksi penjualan baru.
# Melihat total pendapatan dari semua transaksi penjualan.
# Melihat daftar semua transaksi penjualan.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Sale:
    def __init__(self, sale_id, product, quantity, sale_price):
        self.sale_id = sale_id
        self.product = product
        self.quantity = quantity
        self.sale_price = sale_price


class Store:
    def __init__(self):
        self.products = {}
        self.sales = []
        self.next_product_id = 1
        self.next_sale_id = 1

    def add_product(self, name, price):
        product = Product(self.next_product_id, name, price)
        self.products[self.next_product_id] = product
        self.next_product_id += 1
        print(f"Added product: {product.name}, ID: {product.product_id}, Price: {product.price}")

    def add_sale(self, product_id, quantity, sale_price):
        if product_id not in self.products:
            print(f"Product ID {product_id} not found")
            return

        product = self.products[product_id]
        sale = Sale(self.next_product_id, product, quantity, sale_price)
        self.sales.append(sale)
        self.next_sale_id += 1
        print(f"Added sale: sale ID: {sale.sale_id}, Product: {product.name}, Quantity: {quantity}, Sale Price: {sale_price}")

    def total_revenue(self):
        return sum(sale.quantity * sale.sale_price for sale in self.sales)

    def list_sales(self):
        for sale in self.sales:
            print(f"Sale ID: {sale.sale_id}, Product: {sale.product.name}, Quantity: {sale.quantity}, Sale Price: {sale.sale_price}")

# penggunaan
store = Store()
store.add_product('Laptop', 1500)
store.add_product('phone', 280000)

store.add_sale(1, 2, 1003000)
store.add_sale(2,1,40000)

print("\nTotal Revenue:")
print(store.total_revenue())

print("\nAll Sales:")
store.list_sales()
'''
Tujuan:

Latihan ini bertujuan untuk membantu Anda memahami konsep pemrograman berorientasi objek (OOP) dalam Python dengan menerapkannya pada studi kasus pembelian barang.

Deskripsi:

Anggaplah Anda memiliki toko online yang menjual berbagai macam produk.
Anda ingin membuat program Python untuk melacak pembelian pelanggan. Program ini harus dapat:

Menyimpan informasi tentang produk, seperti nama, harga, dan stok.
Mencatat pembelian pelanggan, termasuk produk yang dibeli, jumlah, dan harga total.
Menghitung diskon berdasarkan jumlah pembelian.
Mencetak struk pembelian.
'''

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_total_price(self, quantity):
        return self.price * quantity

    def update_stock(self, quantity):
        self.stock -= quantity

class Purchase:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total_price = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))
        self.total_price += product.get_total_price(quantity)

    def calculate_discount(self, discount_rate):
        self.total_price *= (1 - discount_rate)

    def print_receipt(self):
        print('Struct Pembelian')
        print('Customer:', self.customer)
        print("-----------")
        for product, quantity in self.products:
            print(f"{product.name} X {quantity} : {product.get_total_price(quantity)}")
        print("Total Harga:", self.total_price)

product1 = Product("Laptop", 5000000, 10)
product2 = Product("Mouse", 150000, 20)

purchase = Purchase("Budi", [])
purchase.add_product(product1, 1)
purchase.add_product(product2, 2)

purchase.calculate_discount(0.1) #discount 10%
purchase.print_receipt()


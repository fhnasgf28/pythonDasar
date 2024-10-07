'''
Studi Kasus:
Anda diminta untuk membuat sistem sederhana untuk mengelola penjualan di sebuah toko buku.
Toko buku ini menjual berbagai buku dan mencatat transaksi penjualan.
Setiap transaksi penjualan mencatat buku yang dijual, jumlahnya, dan harga per unit saat transaksi dilakukan.

Sistem harus mendukung fitur berikut:

Menambahkan buku baru ke dalam katalog.
Menambahkan transaksi penjualan baru.
Melihat total pendapatan dari semua transaksi penjualan.
Melihat daftar semua transaksi penjualan.
'''

class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.titla = title
        self.price = price

class Sale:
    def __init__(self, sale_id, book, quantity, sale_price):
        self.sale_id = sale_id
        self.book = book
        self.quantity = quantity
        self.sale_price = sale_price

class BookStore:
    def __init__(self):
        self.books = {}
        self.sales = []
        self.next_book_id = 1
        self.next_sale_id = 1

    def add_book(self, title, price):
        book = Book(self.next_book_id, title, price)
        self.books[self.next_book_id] = book
        self.next_book_id += 1
        print(f"Added book: {book.titla}, ID: {book.book_id}, price: {book.price}")

    def add_sale(self, book_id, quantity, sale_price):
        if book_id not in self.books:
            print(f"Book ID {book_id} not found")
            return

        book = self.books[book_id]
        sale = Sale(self.next_sale_id, book, quantity, sale_price)
        self.sales.append(sale)
        self.next_sale_id += 1
        print(f"Added sale: Sale ID: {sale.sale_id}, Book: {book.titla}, Quantity: {quantity}, Sale Price: {sale_price}")

    def total_revenue(self):
        return sum(sale.quantity * sale.sale_price for sale in self.sales)

    def list_sales(self):
        for sale in self.sales:
            print(f"Sale ID: {sale.sale_id}, Book: {sale.book.titla}, quantity: {sale.quantity}, price: {sale.sale_price}")

# contoh penggunaan
bookstore = BookStore()
bookstore.add_book('Python Programming', 30)
bookstore.add_book('Data Science with Python', 45)
bookstore.add_sale(1,2,343)
bookstore.add_sale(2,3,6000)

print('\nTotal Revenue')
print(bookstore.total_revenue())

print('\nALL Sales:')
bookstore.list_sales()

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
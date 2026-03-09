class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Menambahkan buku ke perpustakaan."""
        self.books.append(book)

    def count_books(self):
        """Menghitung total jumlah buku di perpustakaan."""
        return len(self.books)

    def list_books(self):
        """Menampilkan daftar semua buku di perpustakaan."""
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}')


# Contoh penggunaan
library = Library()

# Menambahkan buku ke perpustakaan
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

library.add_book(book1)
library.add_book(book2)

# Menghitung jumlah buku
total_books = library.count_books()
print(f'Jumlah total buku di perpustakaan: {total_books}')

# Menampilkan daftar buku
library.list_books()
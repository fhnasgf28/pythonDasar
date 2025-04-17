from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Objek yang ditambahkan harus berupa instance dari kelas Book.")

    def get_all_books(self):
        return self.books

    def display_books(self):
        if not self.books:
            print("Perpustakaan kosong.")
            return
        print("Daftar Buku di Perpustakaan:")
        for book in self.books:
            print(book)
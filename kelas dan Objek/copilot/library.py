class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(
            "f{book.title} by {book.author} successfully added to the library."
        )

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{book.title} by {book.author} successfully removed from the library.")
                return
        print(f"Book with title {title} not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

    # membuat instance dari library
library = Library()

    # membuat beberapa buku
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

    # menambahkan buku ke library
library.add_book(book1)
library.add_book(book2)

    # menghapus buku dari library
library.remove_book("The Hobbit")

    # menampilkan daftar buku di library
library.display_books()


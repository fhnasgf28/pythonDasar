from models import Book

class BookController:
    def __init__(self):
        self.books = {}

    def create_book(self, book_id, title, author, year):
        if book_id in self.books:
            print("""Book with ID {} already exists.""".format(book_id))
            return
        book = Book(book_id, title, author, year)
        self.books[book_id] = book
        print("""Book with ID {} created.""".format(book_id))
        print(f"Title: {book.title}, Author: {book.author}, Year: {book.year} successfully created.")

    def read_book(self, book_id):
        book = self.books.get(book_id)
        if book:
            print(book)
        else:
            print(f"Book with ID {book_id} not found.")

    def update_book(self, book_id, title=None, author=None, year=None):
        book = self.books.get(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if year:
                book.year = year
            print(f"Book with ID {book_id} successfully updated.")
        else:
            print(f"Book with ID {book_id} not found.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book with ID {book_id} successfully deleted.")
        else:
            print(f"Book with ID {book_id} not found.")
from datetime import datetime


class LibraryItem:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_date})"


class Book(LibraryItem):
    def __init__(self, title, author, publication_date, isbn):
        super().__init__(title, author, publication_date)
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}({self.publication_date}) - ISBN: {self.isbn}"


class AudioBook(Book):
    def __init__(self, title, author, publication_date, isbn, narrator):
        super().__init__(title, author, publication_date, isbn)
        self.narrator = narrator


class Borrower:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_items = []

    def borrow_item(self, item):
        self.borrowed_items.append(item)


class Library:
    def __init__(self):
        self.items = []
        self.borrowers = []

    def add_item(self, item):
        self.items.append(item)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)


# Test the classes
library = Library()

book = Book("To Kill a Mockingbird", "Harper Lee", datetime(1960, 7, 11), "9780061120084")
audiobook = AudioBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", datetime(1979, 10, 12), "9780307278111", "Stephen Fry")
borrower = Borrower("John Doe", "Johndoe@example.com")

library.add_item(book)
library.add_item(audiobook)
library.add_borrower(borrower)

borrower.borrow_item(book)
borrower.borrow_item(audiobook)

print(borrower.borrowed_items)

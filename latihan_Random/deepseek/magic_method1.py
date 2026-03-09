class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Status: {status}"

    def __repr__(self):
        return f"Book('{self.id}', '{self.title}', '{self.author}', is_borrowed={self.is_borrowed})"

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            return True
        else:
            print(f"Book '{book.title}' is already borrowed.")

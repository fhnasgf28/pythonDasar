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
        return f"Book(id={self.id}, title={self.title}, author={self.author}, is_borrowed={self.is_borrowed})"


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
        else:
            print(f"Book '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            print(f"Book '{book.title}' is not borrowed by {self.name}.")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

    def __repr__(self):
        return f"Member(id={self.id}, name={self.name}, borrowed_books={self.borrowed_books})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.id != book_id]

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.id != member_id]

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        if isinstance(item, Book):
            return item in self.books
        elif isinstance(item, Member):
            return item in self.members
        return False

    def __str__(self):
        book_list = "\n".join(str(book) for book in self.books)
        member_list = "\n".join(str(member) for member in self.members)
        return f"Library:\nBooks:\n{book_list}\nMembers:\n{member_list}"

    def __repr__(self):
        return f"Library(books={self.books}, members={self.members})"
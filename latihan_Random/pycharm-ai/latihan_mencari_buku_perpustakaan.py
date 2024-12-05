class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

# Example usage:
if __name__ == "__main__":
    library = Library()
    book1 = Book("Python Programming", "John Doe", "1234567890")
    book2 = Book("Learning Python", "Jane Doe", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    print("Search by title 'Python':", library.search_by_title("Python"))
    print("Search by author 'Doe':", library.search_by_author("Doe"))
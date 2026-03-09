class Library:
    def __init__(self,):
        self.books = []

    def add_book(self, title, author):
        book = {'title': title, 'author': author}
        self.books.append(book)
        print(f"{title} by {author} successfully added to the library.")

    def display_books(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}")
            print(f"{len(self.books)} books in the library.")

# contoh penggunaan
library = Library()

# menambahkan buku ke perpustakaan
library.add_book("Harry Potter", "J.K. Rowling")
library.add_book("The Hobbit", "J.R.R. Tolkien")

# menampilkan daftar buku di perpustakaan
library.display_books()
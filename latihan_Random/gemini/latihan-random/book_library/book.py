class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.publication_year})"
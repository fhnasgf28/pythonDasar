# Sample book data
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]


# define a function to sort the books
def sort_books(books, key):
    return sorted(books, key=lambda x: x[key])


# sort the books by title
sorted_books_by_title = sort_books(books, "title")
print("Sorted by title:")
for book in sorted_books_by_title:
    print(f"{book["title"]} by {book["author"]} ({book["year"]})")

#Sort the books by author
sorted_books_by_author = sort_books(books, "author")
print("\nSorted by author:")
for book in sorted_books_by_author:
    print(f"{book['title']} by {book['author']} ({book['year']})")

# Sort the books by year
sorted_books_by_year = sort_books(books, "year")
print("\nSorted by year:")
for book in sorted_books_by_year:
    print(f"{book['title']} by {book['author']} ({book['year']})")

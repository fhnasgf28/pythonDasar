from .book import Book

class SearchEngine:
    def search_by_title(self, library, keyword):
        results = [book for book in library.get_all_books() if keyword.lower() in book.title.lower()]
        print(f"Search results for '{results}")

    def search_by_author(self, library, keyword):
        results = [book for book in library.get_all_books() if keyword.lower() in book.author.lower()]
        print(f"Search results for '{results}")
        return results

    def search_by_isbn(self, library, isbn):
        results = [book for book in library.get_all_books() if book.isbn == isbn]
        return results

    def search_by_year(self, library, year):
        try:
            year = int(year)
            results = [book for book in library.get_all_books() if book.publication_year == year]
            return results
        except ValueError:
            print("Invalid year format. Please enter a valid year.")
            return []

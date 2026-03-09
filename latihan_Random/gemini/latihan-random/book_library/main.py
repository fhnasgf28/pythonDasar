from .library import Library
from .book import Book
from .search_engine import SearchEngine

def main():
    library = Library()
    search_engine = SearchEngine()

    # tambahkan beberapa buku ke perpustakaan
    library.add_book(Book("Harry Potter", "J.K. Rowling", "1234567890", 2003))
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "0987654321", 1937))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "1111111111", 1960))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", "2222222222", 1813))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "3333333333", 1925))

    while True:
        print("\nMenu:")
        print("1. Tampilkan semua buku")
        print("2. Cari buku berdasarkan judul")
        print("3. Cari buku berdasarkan penulis")
        print("4. Cari buku berdasarkan ISBN")
        print("5. Cari buku berdasarkan tahun terbit")
        print("6. Keluar")
        choice = input("Masukkan pilihan: ")
        if choice == "1":
            library.display_books()
        elif choice == "2":
            keyword = input("Masukkan kata kunci pencarian: ")
            results = search_engine.search_by_title(library, keyword)
            display_search_results(results)
        elif choice == "3":
            keyword = input("Masukkan kata kunci pencarian: ")
            results = search_engine.search_by_author(library, keyword)
            display_search_results(results)
        elif choice == "4":
            keyword = input("Masukkan kata kunci pencarian: ")
            results = search_engine.search_by_isbn(library, keyword)
            display_search_results(results)
        elif choice == "5":
            keyword = input("Masukkan kata kunci pencarian: ")
            results = search_engine.search_by_year(library, keyword)
            display_search_results(results)
        elif choice == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def display_search_results(results):
    if results:
        for book in results:
            print(f"Judul: {book.title}")
            print(f"Penulis: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Tahun Terbit: {book.publication_year}")
            print("--------------------")
    else:
        print("Buku tidak ditemukan.")

if __name__ == "__main__":
    main()
from controller import BookController

def main():
    controller = BookController()

    while True:
        print("\n--- Book Management ---")
        print("1. Create Book")
        print("2. Read Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year: ")
            controller.create_book(book_id, title, author, year)

        elif choice == '2':
            book_id = input("Enter Book ID: ")
            controller.read_book(book_id)

        elif choice == '3':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title (Leave blank to keep current): ")
            author = input("Enter Author (Leave blank to keep current): ")
            year = input("Enter Year (Leave blank to keep current): ")
            controller.update_book(book_id, title or None, author or None, year or None)

        elif choice == '4':
            book_id = input("Enter Book ID: ")
            controller.delete_book(book_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

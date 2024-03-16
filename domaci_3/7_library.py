class Book:
    def __init__(self, title, author, year, copies):
        self._title = title
        self._author = author
        self._year = year
        self._copies = copies

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_copies(self):
        return self._copies

    def set_copies(self, copies):
        self._copies = copies


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from inventory.")
                return
        print(f"Book '{title}' not found in inventory.")

    def search_books_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.get_title().lower()]
        return found_books

    def search_books_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.get_author().lower()]
        return found_books

    def display_books(self):
        if not self.books:
            print("Library inventory is empty.")
        else:
            print("Books currently available in the library:")
            for book in self.books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}, Copies: {book.get_copies()}")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books by Title")
        print("4. Search Books by Author")
        print("5. Display Books")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, year, copies)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter title to search: ")
            found_books = library.search_books_by_title(title)
            if found_books:
                print("Books found:")
                for book in found_books:
                    print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}, Copies: {book.get_copies()}")
            else:
                print("No books found with the given title.")

        elif choice == '4':
            author = input("Enter author to search: ")
            found_books = library.search_books_by_author(author)
            if found_books:
                print("Books found:")
                for book in found_books:
                    print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}, Copies: {book.get_copies()}")
            else:
                print("No books found by the given author.")

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()

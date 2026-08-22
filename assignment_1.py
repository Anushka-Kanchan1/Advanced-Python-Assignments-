class Book:
    def __init__(self, book_id, title, author, price):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__price = price

    # Properties for encapsulation
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    def category(self):
        if self.__price >= 500:
            return "Premium"
        else:
            return "Standard"

    def display(self):
        print(f"{self.book_id:<10} {self.title:<25} "
              f"{self.author:<20} ₹{self.price:<10} {self.category()}")


class PremiumBook(Book):
    def category(self):
        return "Premium"


class StandardBook(Book):
    def category(self):
        return "Standard"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("\nBook added successfully!")

    def display_books(self):
        if not self.books:
            print("\nNo books available in the library.")
            return

        print("\n" + "=" * 85)
        print("                 LIBRARY BOOK RECORDS")
        print("=" * 85)

        print(f"{'Book ID':<10} {'Title':<25} {'Author':<20} "
              f"{'Price':<10} {'Category'}")

        print("-" * 85)

        for book in self.books:
            book.display()

        print("=" * 85)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found:")
                book.display()
                return

        print("\nBook not found!")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("\nBook deleted successfully!")
                return

        print("\nBook not found!")


def main():

    library = Library()

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        print("===============================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                price = float(input("Enter Book Price: "))

                if price < 0:
                    print("Price cannot be negative.")
                    continue

                if price >= 500:
                    book = PremiumBook(book_id, title, author, price)
                else:
                    book = StandardBook(book_id, title, author, price)

                library.add_book(book)

            except ValueError:
                print("\nInvalid input! Please enter correct values.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":

            try:
                book_id = int(input("Enter Book ID to search: "))
                library.search_book(book_id)
            except ValueError:
                print("\nInvalid Book ID!")

        elif choice == "4":

            try:
                book_id = int(input("Enter Book ID to delete: "))
                library.delete_book(book_id)
            except ValueError:
                print("\nInvalid Book ID!")

        elif choice == "5":
            print("\nThank you for using Library Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Program starts here
if __name__ == "__main__":
    main()


OUTPUT

========== LIBRARY MANAGEMENT SYSTEM ==========
1. Add Book
2. Display All Books
3. Search Book
4. Delete Book
5. Exit
===============================================
Enter your choice: 1

Enter Book ID: 101
Enter Book Title: Python Programming
Enter Author Name: John Smith
Enter Book Price: 650

Book added successfully!

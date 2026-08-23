class Book:

    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        return "Premium" if self.price >= 1000 else "Standard"

    def __str__(self):
        return (
            f"{self.book_id} | {self.title} | "
            f"{self.author} | Rs.{self.price} | {self.category()}"
        )


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display(self):
        print("\nLIBRARY BOOK RECORDS")
        print("--------------------")

        for book in self.books:
            print(book)


library = Library()

library.add_book(Book(101, "Python", "John", 1200))
library.add_book(Book(102, "Data Structures", "Mark", 800))
library.add_book(Book(103, "OOP Concepts", "David", 1500))

library.display()


OUTPUT

LIBRARY BOOK RECORDS
--------------------
101 | Python | John | Rs.1200 | Premium
102 | Data Structures | Mark | Rs.800 | Standard
103 | OOP Concepts | David | Rs.1500 | Premium

"""My sixth day practicing Python."""

class Book:
    """Represent a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        """Borrow the book if it is available."""
        if self.is_borrowed:
            return False

        self.is_borrowed = True
        return True

    def return_book(self):
        """Return the book to the library."""
        self.is_borrowed = False

    def describe(self):
        """Return information about the book."""
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.title} by {self.author} - {status}"


class Member:
    """Represent a library member."""

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book and store it for the member."""
        if book.borrow():
            self.borrowed_books.append(book)
            return True

        return False

    def return_book(self, book):
        """Return a book borrowed by the member."""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True

        return False

    def show_books(self):
        """Show all books borrowed by the member."""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
            return

        print(f"{self.name}'s borrowed books:")

        for book in self.borrowed_books:
            print(f"- {book.title}")


class Library:
    """Manage books and members."""

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def add_member(self, member):
        """Add a member to the library."""
        self.members.append(member)

    def find_book(self, title):
        """Find a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def show_books(self):
        """Display all books in the library."""
        print(f"\nBooks in {self.name}:")

        for book in self.books:
            print(f"- {book.describe()}")

    def library_summary(self):
        """Return library statistics."""
        total_books = len(self.books)
        borrowed_books = sum(book.is_borrowed for book in self.books)
        available_books = total_books - borrowed_books

        return {
            "total_books": total_books,
            "borrowed_books": borrowed_books,
            "available_books": available_books,
            "members": len(self.members),
        }


def main():
    """Run the examples from my sixth Python practice day."""

    print("Welcome to Python practice day 6!")
    print("Today I am building a small Library Management System.")

    library = Library("Ahmed's Python Library")

    book_one = Book("Python Basics", "Eric Matthes")
    book_two = Book("Clean Code", "Robert C. Martin")
    book_three = Book("Automate the Boring Stuff", "Al Sweigart")

    library.add_book(book_one)
    library.add_book(book_two)
    library.add_book(book_three)

    member = Member("Ahmed")
    library.add_member(member)

    library.show_books()

    print("\nSearching for a book...")

    found_book = library.find_book("Clean Code")

    if found_book:
        print(f"Found: {found_book.describe()}")
    else:
        print("Book not found.")

    print("\nBorrowing a book...")

    if member.borrow_book(book_one):
        print(f"{member.name} borrowed '{book_one.title}'.")
    else:
        print("Book is already borrowed.")

    library.show_books()
    member.show_books()

    print("\nReturning the book...")

    if member.return_book(book_one):
        print(f"{member.name} returned '{book_one.title}'.")
    else:
        print("This member does not have that book.")

    library.show_books()

    summary = library.library_summary()

    print("\nLibrary Summary")
    print(f"Total books: {summary['total_books']}")
    print(f"Borrowed books: {summary['borrowed_books']}")
    print(f"Available books: {summary['available_books']}")
    print(f"Members: {summary['members']}")


if __name__ == "__main__":
    main()
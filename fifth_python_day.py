"""My fifth day practicing Python."""


class Book:
    """Represent one book in a reading tracker."""

    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.pages_read = 0

    def describe(self):
        """Return a readable description of the book."""
        return f"{self.title} by {self.author} ({self.total_pages} pages)"

    def read_pages(self, pages):
        """Record pages read without going beyond the end of the book."""
        self.pages_read = min(self.pages_read + pages, self.total_pages)

    def is_finished(self):
        """Return True when every page has been read."""
        return self.pages_read == self.total_pages

    def progress_summary(self):
        """Return a dictionary with the current reading progress."""
        return {
            "title": self.title,
            "pages_read": self.pages_read,
            "pages_remaining": self.total_pages - self.pages_read,
        }


print("Welcome to Python practice day 5!")
print("Today I am learning the basics of Python classes.")

current_book = Book("Python Basics", "Ahmed", 120)
print("Current book:", current_book.describe())

current_book.read_pages(35)
print(f"Pages read today: {current_book.pages_read}")

if current_book.is_finished():
    print("I finished the book!")
else:
    print("I still have some pages to read.")

summary = current_book.progress_summary()
print(f"Pages remaining: {summary['pages_remaining']}")

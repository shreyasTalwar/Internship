# Parent class 1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Parent class 2
class Member:
    def __init__(self, issued_to):
        self.issued_to = issued_to

    def display_member_details(self):
        print("Issued To:", self.issued_to)


# Child class (Multiple Inheritance)
class IssuedBook(Book, Member):
    def __init__(self, title, author, issued_to, issued_date):
        Book.__init__(self, title, author)
        Member.__init__(self, issued_to)
        self.issued_date = issued_date

    def display_issued_book_details(self):
        self.display_book_details()
        self.display_member_details()
        print("Issued Date:", self.issued_date)


# Creating object
book1 = IssuedBook(
    "Python Programming",
    "Guido van Rossum",
    "Shreyas",
    "04-02-2026"
)

# Display all details
book1.display_issued_book_details()

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - $ {self.price:.2f}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"


b1 = Book("Clean Code", "Robert C. Martin", 450.0)
b2 = Book("The Pragmatic Programmer", "Andrew Hunt", 500.0)

print(b1)
print(b2)

books = [b1, b2]
print(books)

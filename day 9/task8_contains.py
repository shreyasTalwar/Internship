class Library:
    def __init__(self, books):
        self._books = list(books)

    def __contains__(self, item):
        return item in self._books


library = Library(["Python", "Java", "C++"])
print("Python" in library)
print("Go" in library)

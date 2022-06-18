# Inheritance is an "is-a" relationship. Composition is a "has-a".
class BookShelf:  # bookshelf contains/composes of/has books
    def __init__(self, *books):  # books is bunch of book objects
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
print(book)

book2 = Book("Python 101")
print(book2)

shelf = BookShelf(book, book2)
print(shelf)

print(shelf.books)

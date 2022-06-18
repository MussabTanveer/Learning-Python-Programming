class ClassTest:
    def instance_method(self):  # used when you want to use/modify data of object
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):  # used often as factories
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():  # used to just place a method inside a class maybe for code organization
        print(f"Called static_method")


test = ClassTest()
test.instance_method()
# OR
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()


# Factory example for class method
class Book:
    TYPES = ("hardcover", "paperback")  # property of class

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book = Book("Harry Potter", "comic book", 1500)
print(book)
# Now use factories
book2 = Book.hardcover("Harry Potter", 1500)  # no need to pass book type
print(book2)
book3 = Book.paperback("Python 101", 600)  # no need to pass book type
print(book3)

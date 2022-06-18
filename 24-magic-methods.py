class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # this will be called when we try to print an object
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):  # this will be called is __str__ is not available, used for debugging
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob)

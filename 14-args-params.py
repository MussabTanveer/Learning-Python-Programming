def add(x, y):
    # pass
    result = x + y
    print(result)


add(5, 3)


def say_hello(name, surname):
    print(f"Hello, {name} {surname}!")


say_hello("Bob", "Smith")
say_hello(surname="Bob", name="Smith")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(15, divisor=0)

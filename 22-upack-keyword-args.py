def named(**kwargs):
    print(kwargs)  # a dictionary


named(name="Bob", age=25)


def named2(name, age):
    print(name, age)  # a dictionary


details = {"name":"Bob", "age": 25}
named2(**details)
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


def my_function(**kwargs):
    print(kwargs)


my_function(**"Bob")  # Error, must be mapping
my_function(**None)  # Error

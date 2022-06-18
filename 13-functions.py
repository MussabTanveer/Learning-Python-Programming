def hello():
    print("Hello!")


hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")


print("Welcome")
user_age_in_seconds()
print("Goodbye!")

friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    print(f)


add_friend()
print(friends)


def add_friend2():
    friends2.append("Rolf")


friends2 = []
add_friend2()
print(friends2)
add_friend2()
print(friends2)
add_friend2()
print(friends2)

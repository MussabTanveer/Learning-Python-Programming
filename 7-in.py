friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter sth you watched: ")
print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == "y":
if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        # elif number - user_number in (1, -1):
        print("You were off by one")
    else:
        print("Sorry, it's wrong")

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
print(longer_phrase.format("Rolf", "Monday"))

size_input = input("How big is your house (in square feet): ") # 500
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")

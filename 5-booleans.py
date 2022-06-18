print("Numbers")
print(5 == 5)
print(5 > 5)
print(10 != 10)

print("Lists")
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad)
print(friends is abroad)
local = friends # points to same memory location
print(friends is local)

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]  # list comp
# Long version
# for num in numbers:
#     doubled.append(num * 2)
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # contain list of friends that start with an S
# Long version
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
print(starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))

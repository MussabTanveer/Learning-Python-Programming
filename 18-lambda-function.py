# lambda doesn't have a name, only used to return values, never used to perform actions
def add(x, y):
    return x + y


print(add(5, 7))

# rewrite above func like below
add2 = lambda x, y: x + y
print(add2(3, 2))

# rewrite above func like below
print((lambda x, y: x + y)(4, 5))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]  # list comp is faster than map
# Or
doubled = map(double, sequence)
# Or
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)

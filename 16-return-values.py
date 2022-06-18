def add(x, y):
    print(x + y)


add(5, 8)
result = add(5, 8)
print(result)  # None is the default return val


def add2(x, y):
    return x + y


result = add2(5, 8)
print(result)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3)
print(result)
result = divide(15, 0)
print(result)
result = divide(15, 0) * 5
print(result)
result = divide(15, 2) * 5
print(result)

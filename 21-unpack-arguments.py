def multiply(*args):
    print(args)  # tuple of args
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 5))
print(multiply(-1))


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))
print(add(x=3, y=5))
nums2 = {"x": 15, "y": 25}
print(add(nums2["x"], nums2["y"]))
print(add(x=nums2["x"], y=nums2["y"]))
print(add(**nums2))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)  # unpack args tuple
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))

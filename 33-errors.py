def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


# Program 1

print("Welcome to the average grade program.")
grades = [78, 99, 85, 100]
average = divide(sum(grades), len(grades))
print(f"The average grade is {average}.")

grades2 = []
try:
    average2 = divide(sum(grades2), len(grades2))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
except ValueError:
    pass
except TypeError:
    pass
except RuntimeError:
    pass
else:  # if no error
    print(f"The average grade is {average2}.")
finally:  # always execute
    print("Thank you!")


# Program 2

print("***************************************")
print("Welcome to the average grade program 2.")
students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")

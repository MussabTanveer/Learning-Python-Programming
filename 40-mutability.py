a = []
b = a

print(id(a))
print(id(b))

a.append(35)

print(a)
print(b)

print(id(a))  # mem loc same as before
print(id(b))  # mem loc same as before

c = ()

# c.append(22) --> error as tuples are immutable

d = 8597
e = 8597  # same as d

print(id(d))
print(id(e))  # same mem loc as d as both have identical values, python does that

d = 8598  # doing that won't change value of e but of d

print(id(d))  # mem loc changed
print(id(e))  # mem loc same as before

# most things in python are mutable except for tuples, strings, integers, floats, booleans
# if you want to make anything immutable, just don't allow it to be changed via methods, etc.

f = "hello"
g = f

print(id(f))
print(id(g))

f += " world"

print(id(f))  # mem loc changed
print(id(g))  # mem loc same as before

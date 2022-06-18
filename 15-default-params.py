def add(x, y=8):  # default params must go at the end
    print(x + y)


add(5)
add(x=5)
# add(y=5) error
add(2, 4)

default_y = 3


def add2(x, y=default_y):
    print(x + y)


add2(2)
default_y = 4  # no impact on func param
add2(2)  # still same result as the val was binded at the time of defining

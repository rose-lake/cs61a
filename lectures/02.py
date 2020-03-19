# Imports
from math import pi
pi * 71 / 223
from math import sin
sin(pi/2)

# Assignment
radius = 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius
print("radius", radius, "area", area, "circ", circ)
radius = 20
print("radius", radius, "area", area, "circ", circ)

# Function values
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# f(3, 4)
__builtins__.max

# User-defined functions
from operator import add, mul

def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# area function
def area():
    return pi * radius * radius
print("radius", radius, "area()", area())
radius = 20
print("radius", radius, "area()", area())
radius = 10
print("radius", radius, "area()", area())

# Name conflicts
# note: there is no conflict here!
def square(square):
    return mul(square, square)
square(4)

# swapping names
# With multiple assignment, all expressions to the right of = are evaluated before any names to the left are bound to those values. As a result of this rule, swapping the values bound to two names can be performed in a single statement.

x, y = 3, 4.5
print("x", x, "\ty", y)
y, x = x, y
print("x", x, "\ty", y)

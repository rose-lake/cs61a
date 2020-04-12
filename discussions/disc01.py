# Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
# Write a function that takes in the current temperature and a boolean value telling
# if it is raining and returns True if Alfonso will wear a jacket and False otherwise.

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60:
        return True
    elif raining:
        return True
    else:
        return False

# Note that we’ll either return True or False based on a single condition, whose
# truthiness value will also be either True or False. Knowing this, try to write this
# function using a single line.

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

# question 1.2 :: What is the result of executing the following code? an infinite loop!
def square(x):
    print("here!")
    return x * x
def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
# square(so_slow(5))
# the result is an infinite loop

# question 1.3 :: Write a function that returns True if a positive integer n is a prime number and False otherwise.
from math import sqrt
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    assert n > 0, 'n must be positive'
    if n == 1:
        return False
    k = 2
    while k < sqrt(n):
        if n % k == 0:
            return False
        k = k + 1
    return True

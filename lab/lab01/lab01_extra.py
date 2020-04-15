"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    factorial = 1
    while k:
        factorial = n * factorial
        n, k = n-1, k-1
    return factorial

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # take last digit of n, and set n = n without the final digit
    n, digit = n // 10, n % 10

    # loop so long as n has more digits to parse
    while n:
        new_digit = n % 10
        if digit == 8 and new_digit == 8:
            return True
        # parse the next digit of n
        n, digit = n // 10, new_digit

    return False


# use built-in function pow, and convert it to a curried function curried_pow

def curried_pow(x):
    '''Using curried_pow you can do things like

    >>> three_to_the = curried_pow(3)
    >>> three_to_the(5)
    243

    >>> four_to_the = curried_pow(4)
    >>> four_to_the(2)
    16
    '''
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    '''Using map_to_range you can do things like

    >>> map_to_range(0, 10, curried_pow(2))
    1
    2
    4
    8
    16
    32
    64
    128
    256
    512
    '''
    while start < end:
        print(f(start))
        start = start + 1

# we can manually implement currying and uncurrying for two-argument functions
def curry2(f):
    '''Return a curried version of the given two-argument function f'''
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    '''Return a two-argument version of the given curried function.'''
    def f(x, y):
        return g(x)(y)
    return f

# Then, we can do stuff like:
# >>> pow_curried = curry2(pow)
# >>> pow_curried(2)(5)
# 32
# >>> map_to_range(0, 10, pow_curried(2))
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512

# original code is at https://composingprograms.com/pages/16-higher-order-functions.html#function-decorators

def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3*x

# Extra for experts. The decorator symbol @ may also be followed by a call expression.
    # 1. The expression following @ is evaluated first (just as the name trace was evaluated above),
    # 2. the def statement second,
    # 3. and finally the result of evaluating the decorator expression is applied to the newly defined function, and the result is bound to the name in the def statement.

# there is purpotedly a tutorial written by Ariel Ortiz on decorators, but it can't be found at present...

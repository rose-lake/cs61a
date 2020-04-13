from improve_iterator_pattern import improve, approx_eq

##################################################
# newton's general method for approximating roots
##################################################

# original code at https://composingprograms.com/pages/16-higher-order-functions.html#example-newton-s-method

# newton's method is an iterative improvement algorithm
# it improves the guess of the zero for any differentiable function.

# derivative of f at x :: the slope of f at x
# slope is a ratio :: change in function value: f(x) / change in function argument: x

# translating your guess 'x' by f(guess)/df(guess)
# gives you the new x-value (new guess) at the zero of the tangent df(x)
# in other words, the new x-value is the zero of the slope at the previous x-value
# this converges to the x-value of the zero of the function f(x)


# a caveat from the text:
# As you experiment with Newton's method, be aware that it will not always converge. The initial guess of improve must be sufficiently close to the zero, and various conditions about the function must be met. Despite this shortcoming, Newton's method is a powerful general computational method for solving differentiable equations. Very fast algorithms for logarithms and large integer division employ variants of the technique in modern computers.

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

##################################################
# newton's general method applied to square roots
##################################################
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

###############################################
# newton's general method applied to nth roots
###############################################
# since a root is, by definition x * x * x * .... * x = a
#     where a is the number whose root you wish to find
#     and x is repeated n times
#     where n is the nth root of a
#
# then, you can adapt this relationship to be : x^n - a = 0
# thus, when you wish to find the nth root of a,
#     you are searching for the zeros of the function x^n - a
#
# translated into newton's general method, this would look like so
#     new_guess = old_guess - (old_guess^n - a) / (n * old_guess ^ (n-1))

def power(x, n):
        """Return x * x * x * ... * x for x repeated n times."""
        product, k = 1, 0
        while k < n:
            product, k = product * x, k + 1
        return product

def nth_root_of_a(n, a):
    def f(x):
        # return x**n - a
        return power(x,n) - a
    def df(x):
        # return n * x**(n-1)
        return n * power(x, n-1)
    return find_zero(f, df)

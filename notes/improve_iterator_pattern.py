
# see http://composingprograms.com/pages/16-higher-order-functions.html
# for original code on all of these patterns

############################
# improve iterator pattern
############################

def improve(update, close, guess=1):
    '''
    generic improve iterator pattern
    defined with an 'update' function and a 'close' function
    starts with a seed (guess) equal to 1
    '''
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-15):
    '''
    approx_eq checks the difference of its two arguments against a desired tolerance.
    tolerance is set to 1e-15 by default
    absolute value of the difference is used
    '''
    return abs(x - y) < tolerance

def average(x, y):
    ''' our own implementation of a simple average function '''
    return (x + y)/2

#####################################
# Golden-ratio or Phi implementation
#####################################
def phi_update(guess):
    '''phi_update :: iterative approximation to phi...
        to begin ::
            start with any positive number
            our improve pattern starts with a seed of 1 by default
        to iterate a new guess ::
            take the inverse of your previous guess
            sum it with 1
            treat this as your new guess
    '''
    return 1/guess + 1

def phi_close(guess):
    '''phi_close :: testing the closeness of our guess to actual phi...
        one definition of phi is
            phi*phi - 1 = phi
        by extension,
            phi*phi = phi - 1
        use this fact as our test for closeness
        approx_eq tests for absolute difference < tolerance (1e-15 by default)
    '''
    return approx_eq(guess * guess, guess + 1)

# to test correctness of improve method
# use an alternate definition of phi and compare both results
from math import sqrt
phi = 1/2 + sqrt(5)/2
approx_phi = improve(phi_update, phi_close)
def improve_test():
    ''' no news is good news
    if the function doesn't print anything, it means the assertion passed
    '''
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

##############################
# Square-Root implementation
##############################

# lexical scoping / closure ::
# The improve pattern passes only one parameter, guess, to the update and close funcs
# Whereas the phi implementation was approximating a constant (phi)
# The square root implementation needs to know -which- square root we're seeking
# to solve this, we use lexical scoping, or closure

def sqrt(a):
    '''
    Use the improve pattern to calculate the square root of 'a'

    Uses closure to give sqrt_update and sqrt_close access to 'a', the number whose square root we're seeking.
    '''

    def sqrt_update(guess):
        '''Iterative approximation for a square root

        Assuming guess has been seeded with any positive number, iterate the guess by averaging guess with a/guess.

        Except:
            - This does not work for square root of 8, don't know why.
                - there was a caveat on the general newton's method which simply says: be aware that it will not always converge... the initial guess must be sufficiently close to the zero and various conditions about the function must be met (including differentiable!)
            - If you seed with a negative guess, your result is negative but the absolute value of the result is correct.
                - this is because newton's method (which this is a specific case of), works by converging to the nearest zero (root). if you seed with a negative number, it will converge to the negative root in the case of square roots.
        '''
        print('new guess', average(guess, a/guess))
        return average(guess, a/guess)

    def sqrt_close(guess):
        '''Tests the closeness of our guess to the actual square root
        '''
        print('close enough? ', approx_eq(guess*guess, a))
        return approx_eq(guess * guess, a)

    return improve(sqrt_update, sqrt_close)

    # # seed explicitly to test
    # first_guess = 30
    # print('first guess', first_guess)
    # return improve(sqrt_update, sqrt_close, first_guess)

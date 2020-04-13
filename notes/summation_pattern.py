
# see http://composingprograms.com/pages/16-higher-order-functions.html
# for original code on all of these patterns

####################
# summation pattern
####################
def summation(n, term):
    '''Sum, for k=1 to n, a 'term' defined in k.
    term passed in as a function.
    returns the total sum.
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k+1
    return total

def cube(x):
    return x*x*x

def identity(x):
    return x

def pi_term(x):
    return 8 / ((4*x - 3) * (4*x - 1))

# you can call these directly, or by making functions for them:
def cube_sum(n):
    return summation(n, cube)

def identity_sum(n):
    return summation(n, identity)

def pi_sum(n):
    return summation(n, pi_term)

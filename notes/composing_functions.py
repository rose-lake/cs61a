# original code samples are from
# http://composingprograms.com/pages/16-higher-order-functions.html
def compose1(f, g):
    '''the 1 in the name means each function takes one argument'''
    def h(x):
        return f(g(x))
    return h

def square(x):
    # print('x is ', x, ', squaring x')
    return x * x

def successor(x):
    # print('x is ', x, ', adding 1 to x')
    return x + 1

def f(x):
    '''Never called'''
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)

# lambda implementation of above

def lcompose1(f, g):
    '''An implementation of the compose in 1 argument via a lambda
    This is distinct from returning f(g(x)) which would evaluate the composed functions,
    and furthermore the value of x is not provided.
    Returning the lambda returns the function in x.
    '''
    return lambda x: f(g(x))

f = lcompose1(lambda x: x * x,
              lambda y: y + 1)

lresult = f(12)

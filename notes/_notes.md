# first digits of a^b
The best known method for computing the first digits of a^b is representing it as 10^𝑏∗𝑙𝑜𝑔10(𝑎), finding fractional part of 𝑏∗𝑙𝑜𝑔10(𝑎)=𝑐 and computing 10𝑐. That should be faster than direct computing.
In other words, b * log10(a) = c where c is the decimal place-value of the first digit of a^b
For example, for x=3^95, you get c=45+decimal-fraction which tells you that the first digit is at the 10^45 position.
Note that you must truncate c to its whole-number part only for this to work.
So x // 10^floor(c) returns the value of the first digit. (or you can use trunc(c)).

# code style
https://cs61a.org//articles/composition.html
This is an excellent article that provides a clear and concise overview of good vs bad code style in Python.

# newton's method
for computing the root(s) of a function
iterative method
    new_guess = old_guess - f(old_guess) / df(old_guess)
    where df = derivative of f, or slope of f, evaluated at old_guess

# applied to finding numerical nth-root-of-a
since a root is, by definition x * x * x * .... * x = a
    where a is the number whose root you wish to find
    and x is repeated n times
    where n is the nth root of a

then, you can adapt this relationship to be : x^n - a = 0
thus, when you wish to find the nth root of a,
    you are searching for the zeros of the function x^n - a

translated into newton's general method, this would look like so
    new_guess = old_guess - (old_guess^n - a) / (n * old_guess ^ (n-1))

# 'first class' status -> functions
In general, programming languages impose restrictions on the ways in which computational elements can be manipulated. Elements with the fewest restrictions are said to have first-class status.

Some of the "rights and privileges" of first-class elements are:
- They may be bound to names.
- They may be passed as arguments to functions.
- They may be returned as the results of functions.
- They may be included in data structures.

Python awards functions full first-class status, and the resulting gain in expressive power is enormous.

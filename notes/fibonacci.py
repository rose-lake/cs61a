##############################
# fibonacci iteration example
##############################

def fib(n):
    pred, curr = 0, 1       # 0th and 1st fibonacci numbers
    k = 1                   # curr is the kth fibonacci number; also our index
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    # we increment k at the end of the loop,
    # so when we're done, k == n
    return curr
    # also, curr == kth fibonacci number == nth fibonacci number

# discussion question
# what if the original pred and curr were bound to 1, 0 instead of 0, 1
# would it be the same or different from original fib ?
    # before the while loop:
        # pred = 1
        # curr = 0
        # k = 0
    # first iteration of while loop:
        # pred = 0
        # curr = 1
        # k = 1
    # second iteration:
        # pred = 1
        # curr = 1
        # k = 2
    # third iteration:
        # pred = 1
        # curr = 2
        # k = 3
    # fourth iteration:
        # pred = 2
        # curr = 3
        # k = 4
    # fifth iteration:
        # pred = 3
        # curr = 5
        # k = 5
# fib(5) returns 5 like before
# ** bonus ** we can now compute fib(0) correctly! :)
# the while loop is never run if you pass in n=0, and curr is returned as 0.

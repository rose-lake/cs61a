
# nonlocal, `*args`, assert, and closures
```python
def make_test_dice(*outcomes):
    # *outcomes takes unlimited number of arguments passed into the function and captures them as a tuple
    # essentially, this method could be called 'make_deterministic_dice'

    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    # assert condition is true. if not, raise an AssertError with the associated message
    # assert statements are run if __debug__ is True.
    # __debug__ :: the built-in variable __debug__ is True under normal circumstances,
                    # False when optimization is requested (command line option -o).
    # -o option :: Remove assert statements and any code conditional on the value of __debug__.

    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'

    index = len(outcomes) - 1
    # start index at the LAST POSITION

    def dice():

        nonlocal index
        # nonlocal index causes index to refer to previously bound variable in the nearest enclosing scope, excluding globals.
        # e.g. index refers specifically to the index defined just before def dice():
        # Names listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope.
        # Names listed in a nonlocal statement must not collide with pre-existing bindings in the local scope.

        index = (index + 1) % len(outcomes)
        # before referencing into outcomes tuple, advance index
        # this means in the base case outcomes is indexed at the FIRST POSITION

        return outcomes[index]

    return dice    
```
In the function below, you see how the nonlocal keyword means changes inside function_inside affect 'msg' variable permanently.
So, in make_test_dice, when you modify index, index always stays modified and always 'travels with' your function instance.
It's like a closure creates a local global namespace that thereafter travels around with the function wherever it goes.
Ah! That is so cool! :)
```python
def function_outside():
    msg = 'Hi'
    def function_inside():
        nonlocal msg
        msg = 'Hello'
        print (msg)
    function_inside()
    print (msg)
```

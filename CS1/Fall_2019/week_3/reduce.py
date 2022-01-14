# reduce.py
# By THC.  Shows how variables can be functions.

# Returns the result of applying operation op with
# identity id to combine all the values in a list.
def reduce(the_list, op, id):
    result = id
    for value in the_list:
        result = op(result, value)
    return result

# Return a + b.
def plus(a, b):
    return a + b

# Return a * b.
def times(a, b):
    return a * b

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(reduce(some_list, plus, 0))
print(reduce(some_list, times, 1))

add = plus  # the variable 'add' is actually the 'plus' function
print(add(4, 7))    # calls the 'plus' function
print(reduce(some_list, add, 0))
empty_list = []
multiply = times    # 'multiply' is actually the 'times' function
print(reduce(empty_list, multiply, 1))  # prints the identity: 1
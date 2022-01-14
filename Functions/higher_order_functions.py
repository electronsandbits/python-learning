"""
File:higher_order_functions.py
------------------------------
"""

def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def test_numbers(test_function, numbers):
    return [test_function(n) for n in numbers]

evens = test_numbers(is_even, [1, 2, 3, 4])
positives = test_numbers(is_positive, [-2, -1, 0, 1, 2])

print(evens) # Prints [False, True, False, True]
print(positives) # Prints [False, False, False, True, True]
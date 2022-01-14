"""
File:reduce_functions.py
"""

# The reduce function requires importing
from functools import reduce
def add(x, y):
    return x + y


sum = reduce(add, [1, 2, 3, 4, 5])
print(sum) # Prints 15
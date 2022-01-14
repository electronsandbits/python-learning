"""
File:my_function.py
-------------------
simpler example to show how an unpacking statement
and multiple-return function work the same way:
"""

first, second = 1, 2
assert first == 1
assert second == 2

def my_function():
    return 1, 2
first, second =my_function()
assert first == 1
assert second == 2
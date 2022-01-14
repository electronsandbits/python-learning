"""
File:swap.py
------------
return multiple values from a function, for example in this
swap function the order in which the parameters are supplied is swapped when
they are returned:
"""

def swap(a, b):
    return b, a

a = 7
b = 14
x, y = swap(a, b)
print(x, ',', y)

# Tuple
z = swap(a, b)
print(z)


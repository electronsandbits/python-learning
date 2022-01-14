"""
File:squares.py
---------------
This program the squares of the natural numbers.
"""

squares =[1, 4, 9, 16, 25, 36]
print(squares)

print(squares[0])  # indexing returns the item
print(squares[-1])  # returns the last element
print(squares[-3:]) # prints [16,25,36]
print(squares[:])  # print all list

print(squares + [36, 49, 64, 81, 100])

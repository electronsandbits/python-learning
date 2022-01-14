#
# File:squares.py
# ---------------
# This program make a list of the first 10 square numbers, that is
# the square of each integer from 1 through 10.
#

squares = [] # an empty list
for value in range (1, 11):
    square = value ** 2
    squares.append(square)  # squares.append(value ** 2)

print (squares)   

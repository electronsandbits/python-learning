"""
File:square.py
--------------
Returning Values from Functions
"""

def square(n):
    return n * n

# Store result from square in a variable
result = square(4)
print(result)

# Send the result from square immediately to another function
print(square(5))

# Use the result returned from square in a conditional expression
if square(3) < 15:
    print("Still less than 15")


"""
The following Python program uses the or operator to determine whether or not
the value entered by the user is one of the first 5 prime numbers. The and and not
operators can be used in a similar manner when constructing a complex condition.
"""

# Read an integer from the user
x = int(input("Enter an integer: "))

# Determine if it is one of the first 5 primes and report the result
if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
    print("That's one of the first 5 primes.")
else:
    print("That's is not one of the first 5 primes.")
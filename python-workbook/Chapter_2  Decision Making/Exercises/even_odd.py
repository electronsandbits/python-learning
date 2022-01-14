"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.

even_odd.py
-----------
This program reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.

@author: electronsandbits
@version: December 7,2021
"""

# Read the integer from the user
number = int(input("Enter an integer: "))

# Determine whether it is even or odd by using the modulus(remainder) operator.
if number % 2 == 1:
    print(number, "is odd.")
else:
    print(number, "is even.")
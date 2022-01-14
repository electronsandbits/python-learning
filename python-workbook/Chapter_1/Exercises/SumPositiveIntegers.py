"""
 file:sumPositiveIntegers.py
 ---------------------------
This program reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula: sum = (n)(n + 1) / 2.

@author:@ electronsandbits
@version: December 10, 2021

"""

# Read the value of n from the user
n = int(input("Enter a positive integer:  "))

# Compute the sum
sum = n * (n + 1) / 2

# Display the result
print("The sum is", sum)
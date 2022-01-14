"""
largerOfTwoNumbers.py
---------------------
This program demonstrates an algorithm to
find the larger of two numbers.

@author: electronsandbits
@version: December 9, 2021
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print("The largest number is:", first_number)
elif first_number < second_number:
    print("The largest number is: ", second_number)
else:
    print("The numbers are equal")



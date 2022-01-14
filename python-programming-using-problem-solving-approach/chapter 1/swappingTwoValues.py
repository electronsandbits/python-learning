"""
swappingTwoValues.py
-------------------
This program demonstrates an algorithm for
interchanging/swapping two numbers.

@author: electronsandbits
@version: December 9, 2021
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Before Swapping", first_number, second_number)

temp = first_number
first_number = second_number
second_number = temp
print("After Swapping", first_number, second_number)



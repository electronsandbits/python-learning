"""
Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.

file:AreaOfField.py
-------------------
This  program reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

@author:electronsandbits
@version:December 9, 2021
"""
# Constants
SQFT_PER_ACRE = 43560

# Read the dimensions of the farmer's field from the user
length = float(input("Enter the width of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

# Compute the area of the field
acres = length * width / 43560

# Display the result
print("The area of the field is", acres, "acres")
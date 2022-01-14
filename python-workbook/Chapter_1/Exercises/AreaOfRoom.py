"""
Exercise 3: Area of a Room

Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.

file:AreaOfRoom.py
------------------
This program asks the user to enter the width and length of a room. Once
these values have been read, the program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers.

@author:electronsandbits
@version:December 9, 2021
"""

# Read the dimensions from the user
width = float(input("Enter the width of the room in meters: "))
length = float(input("Enter the width of the room  in meters: "))

# Compute the area of the room
area = width * length

# Display the result
print("The area of the room is", area, "square meters")

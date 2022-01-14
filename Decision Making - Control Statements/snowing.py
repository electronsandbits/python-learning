"""
File:snowing.py
---------------
This program demonstrates nesting if statements.
"""
snowing = True
temperature = 0

if temperature < 0:
    print("It is freezing!")
    if snowing:
        print("Put on boots")
    print("Time for Hot Chocolate")

print("Bye")
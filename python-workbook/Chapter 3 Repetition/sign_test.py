"""
File: SignTest.py
------------------
This code segment reads values from the user and
reports whether each value is positive or negative. The loop terminates when the user
enters 0. Neither message is displayed in this case.
"""

# Read the first value from the user
number = int(input("Enter an integer (0 to quit) : "))

# Keep looping while the user enters a non-zero number
while number != 0:
    # Report the nature of the number
    if number > 0:
        print("That's a positive number.")
    else:
        print("That's a negative number.")

    # Read the next value from the user
    number = int(input("Enter an integer (0 to quit) : "))
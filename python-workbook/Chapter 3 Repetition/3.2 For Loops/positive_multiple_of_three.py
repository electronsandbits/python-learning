"""
File:PositiveMultipleOfThree.py
-------------------------------
The following program uses a for loop and the range function to display all
of the positive multiples of 3 up to (and including) a value entered by the user.
"""

# Read the limit from the user
limit = int(input("Enter an integer: "))

# Display the positive multiples of 3 up to the limit
print("The multiples of 3 up to and including", limit, "are: ")
for i in range(3, limit + 1, 3):
    print(i)
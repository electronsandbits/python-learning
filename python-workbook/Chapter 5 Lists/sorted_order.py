"""
The reverse method reverses the order of the elements in the
list, and the sort method sorts the elements
into ascending order. Both reverse and sort can be applied to a list without
providing any arguments.
The following example reads a collection of numbers from the user and stores
them in a list. Then it displays all of the values in sorted order.
"""

# Create a new, empty list
values = []
# Read values from the user and store them in a list until a blank line is entered
line = input("Enter a number (blank line to quit): ")
while line != "":
    number = float(line)
    values.append(number)
    line = input("Enter a number (blank line to quit): ")

# Sort the values into ascending order
values.sort()

# Display the values
for value in values:
    print(value)


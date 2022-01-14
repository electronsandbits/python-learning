"""
Searching a List
- The in operator is used to determine whether or not a value is present in a list.
- The index method is used to identify the position of a particular value within
a list.
"""

# Read integers from the user until a blank line is entered and store them all in data
data = []
line = input("Enter an integer (blank line to finish): ")
while line != "":
   n = int(line)
   data.append(n)
   line = input("Enter an integer (blank line to finish): ")

# Read an additional integer from the user
x = int(input("Enter one additional integer: "))

# Display the index of the first occurrence of x (if it is present in the list)
if x in data:
    print("The first", x, "is at index", data.index(x))
else:
    print(x, "is not in the list")

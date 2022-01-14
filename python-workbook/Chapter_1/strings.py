"""
the following program reads two strings from the user which are a
person’s first and last names. It then uses string concatenation to construct a new
string which is the person’s last name, followed by a comma and a space, followed
by the person’s first name
"""

# Read the names from the user
first = input("Enter the first name: ")
last = input("Enter the last name: ")

# Concatenate the strings
full_name = last + ", " + first

# Display the result
print(full_name)
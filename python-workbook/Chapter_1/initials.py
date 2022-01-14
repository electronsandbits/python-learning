"""
initials.py
"""

# Reads the user's name
first = input("Enter your first name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name : ")

# Extract the first character from each string and concatenate them
initials = first[0] + middle[0] + last[0]

# Display the initials
print("Your initials  are", initials)
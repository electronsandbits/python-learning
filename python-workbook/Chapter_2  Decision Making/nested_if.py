"""
nested_if.py
"""

# Read a number from the user
number = float(input("Enter a number: "))

# Store the appropriate message in result
if number > 0:
    # Determine what adjective should be used to describe the number
    adjective = " "
    if number >= 1000000:
        adjective = " really big "
    elif number >= 1000:
        adjective = "big "
    # Store the message for positive numbers including the appropriate adjective
    result = "That's a " + adjective + "positive number"
    
elif number < 0:
    result = "That's a negative number"
else:
    result = "That's a zero"

# Display the message
print(result)




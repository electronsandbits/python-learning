"""
File:message.py
---------------
The following program uses a for loop nested inside a while loop
to repeat messages entered by the user until the user enters a blank message.

@author:electronsandbits
@version:December 15, 2021
"""

# Read the first message from the user
message = input("Enter a message (blank to quit):  ")

# Loop until the message is a blank line
while message != "":
    # Read the number of times the message should be displayed
    n = int(input("How many times should it be repeated? "))

    # Display the message the number of times requested
    for i in range(n):
        print(message)

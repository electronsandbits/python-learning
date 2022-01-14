"""
Exercise 5: Bottle Deposits

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.

file:bottleDeposits.py
----------------------
This program reads the number of containers of each size from the user.
The program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.

@author:electronsandbits
@version:December 9, 2021
"""

# Compute the refund amount for a collection of bottles.

# Constants
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

# Read the number of containers of each size from the user
less = int(input("How many containers 1 litre or less? "))
more = int(input("How many containers more than 1 litre? "))

# Compute the refund amount
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

# Display the result
print("Your total refund will be $%.2f." % refund)

# The %.2f format specifier indicates that a value should be formatted
# as a floating-point number with 2 digits to the right of the decimal point.
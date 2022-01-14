# This prints  a different message depending on whether the
# program is executed during December or not.

month = input("Please enter the month: ")

# The following line will only ever execute during December
if month == 12:
    print("It's christmas  time!")
#elif month == 8:
 #    print("Happy Birthday , Frank it's August!")
else:
    # If it’s not December, this line is executed.
    print("Just another ordinary day...")


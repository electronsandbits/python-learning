"""
File:average.py
---------------
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the
average.

@author:electronsandbits
@version: December 15, 2015
"""

"""
 Constant: SENTINEL
 ------------------
 This constant defines the value used to terminate the input list
 and should therefore not be a value one would want to include as a data value.
 The value 0 therefore makes sense for a program that adds a series
 of numbers because the user can simply skip any 0 value in the input.
 """
SENTINEL = 0

print("This program adds a list of numbers. Use", SENTINEL, "to signal the end.")

sum = 0
count = 0
value = 1

# Keep looping while the value is different from SENTINEL
while value != 0:
    # Read the list of values from the user
    value = int(input("Enter a value : "))
    if value == SENTINEL:
        break
    sum += value
    count = count + 1

print("The sum is", sum)
print("The count is", count)
average = sum /count
print("The average is ", average)





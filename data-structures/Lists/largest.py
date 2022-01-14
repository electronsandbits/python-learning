"""
File:largest.py
---------------
This program uses the for loop to iterate over a list's indices
instead of its values.
"""

constants = [2.71, 3.14, 1.41, 1.62]
largest = 0

# Find the position of the largest element
for i in range(1, len(constants)):
    if constants[i] > constants[largest]:
        largest = i

# Display the result
print("The largest value is", constants[largest], "which is at index", largest)

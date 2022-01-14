"""
The following program
demonstrates this by using a for loop to iterate through all of data’s indices, except
the first, to identify the position of the largest element in data.
"""

# Initialize data and largest position
data = [1.62, 1.41, 3.14, 2.71]
largest_position = 0

# Find the position of the largest element
for i in range(1, len(data)):
    if data[i] > data[largest_position]:
        largest_position = i

# Display the result
print("The largest value is", data[largest_position], "which is at index", largest_position)
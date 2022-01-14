"""
Adding Elements to a List

"""
"""
# Adding Elements to a List
data = [2.71, 3.14, 1.41, 1.62]
data.append(2.30)
print(data)

# insert method
data = [2.71, 3.14, 1.41, 1.62]
data.insert(2, 2.30)
print(data)


# Removing Elements from a List
data = [2.71, 3.14, 1.41, 1.62]
data.remove(1.62)  # Remove 1.62 from the list
last = data.pop()  # Remove the last element from the list
print(data)
print(last)



# Rearranging the Elements in a List

# Create a list
data = [2.71, 3.14, 1.41, 1.62]

# Swap the element at index 1 with the element at index 3
temp = data[1]
data[1] = data[3]
data[3] = temp

# Display the modified list
print(data)

"""

T
# Initialize data
data = [0, -1, 4, 1, 0]

# Loop while i is a valid index and the value at index i is not a positive value
i = 0
while i < len(data) and data[i] <= 0:
    i = i + 1

# If i is less than the length of data then the loop terminated because a positive number was
# found. Otherwise i will be equal to the length of data, indicating that a positive number
# was not found.

if i < len(data):
    print("The first positive number is at index", i)

else:
    print("The list does not contain a positive number")

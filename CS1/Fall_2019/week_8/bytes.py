# bytes.py
# Shows how to use Python's bytes and bytearray types.

# Create bytes objects, which are immutable.
b1 = bytes([2, 3, 7, 10])
b2 = bytes((20, 22, 27))
b3 = bytes("abcde", "UTF-8")
print(b1)
print(b2)
print(b3)

# Create a bytes object from a string.
b4 = "fghij".encode()
print(b4)

# Create a bytearray object, which is mutable.
b5 = bytearray([15, 17, 21])
print(b5)

# Make changes to the bytearray object.
b5.append(23)
print(b5)
b5[1] = 30
print(b5)
b5.insert(2, 90)  # 90 is the ASCII code for Z
print(b5)
del b5[1]
print(b5)
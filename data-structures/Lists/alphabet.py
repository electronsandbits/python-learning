"""
File:alphabet.py
----------------
This program prints the letters of the alphabet
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(alphabet)
len(alphabet)

alphabet[2:5] = ['C', 'D', 'E']
print(alphabet)
# now remove them
alphabet[2:5] = []
print(alphabet)

# clear the list by replacing all the elements with an empty list
alphabet[:] = []
print(alphabet)

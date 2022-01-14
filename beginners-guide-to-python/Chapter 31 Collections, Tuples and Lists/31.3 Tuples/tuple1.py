"""
Tuples:
 A Tuple represents a collection of objects that are ordered and immutable
(cannot be modified). Tuples allow duplicate members and are indexed.
"""

list1 = [1, 2, 3]
t1 = tuple(list1)
print(t1)

# Creating Tuples
# The tuple() Constructor Function: tuple(iterable)
tuple1 = (1, 3, 5, 7)

# Accessing Elements of a Tuple
print('tuple1[0]:\t', tuple1[0])
print('tuple1[1]:\t', tuple1[1])
print('tuple1[2]:\t', tuple1[2])
print('tuple1[3]:\t', tuple1[3])

# Creating New Tuples from Existing Tuples
# Which returns a new Tuple of two elements containing
# the elements from index 1 up to (but not including) element 3
print('tuple1[1:3]: \t', tuple1[1:3]) #(3,5)

# if the first index is omitted it indicates that the slice should start from the
# beginning of the tuple, while omitting the last index indicates
# it should go to the end  of the Tuple.

print('tuple1[:3]:\t', tuple1[:3])  # (1,3, 5)
print('tuple1[1:]:\t', tuple1[1:])  # (3, 5, 7)

# Reversing a Tuple
print('tuple1[:: -1]:\t', tuple1[:: -1])

# scan.py
# Performs inclusive and exclusive scan operations on a list.

def plus(a, b):
    return a + b

def times(a, b):
    return a * b

# Perform an inclusive scan operation on my_list, given an operation op.
# When done, my_list[i] should contain the result of the operation
# performed on my_list[0] through my_list[i], and my_list[0] should
# remain unchanged.
def inclusive_scan(my_list, op):
    # YOU FILL THIS IN.

# Perform an exclusive scan operation on my_list, given an operation op
# and the identity id for the operation.  When done, my_list[i] should
# contain the result of the operation performed on my_list[0] through
# my_list[i-1], and my_list[0] should contain the identity.
def exclusive_scan(my_list, op, id):
    # YOU FILL THIS IN.

numbers = [3, 6, 2, 1, 4, 7]
print("The list: ", numbers)
exclusive_scan(numbers, plus, 0)
print("After an exclusive plus-scan:", numbers)

numbers = [3, 6, 2, 1, 4, 7]
print("The list: ", numbers)
inclusive_scan(numbers, plus)
print("After an inclusive plus-scan:", numbers)

numbers = [2, 4, 2, 6, 2]
print("The list: ", numbers)
exclusive_scan(numbers, times, 1)
print("After an exclusive times-scan:", numbers)

numbers = [2, 4, 2, 6, 2]
print("The list: ", numbers)
inclusive_scan(numbers, times)
print("After an inclusive times-scan:", numbers)
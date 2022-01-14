# Iterating Over Tuples

fruits = ('apple', 'pear', 'orange', 'plum', 'apple', 'banana', 'watermelon')
for fruit in fruits:
    print(fruit)

print('len(fruits):\t', len(fruits)) # Length of a tuple
print(fruits.count('apple')) # returns 2
print(fruits.index('pear')) # returns 1

# Checking if an Element Exists
if 'orange' in fruits:
    print('orange is in the Tuple')

# Nested Tuples
odd_numbers = (1, 3, 5, 7)
names = ('Saniyyah', 'Wiltold', 'Yuan', 'Dina')
tuple = (42, odd_numbers, names, 5.5)
print(tuple)


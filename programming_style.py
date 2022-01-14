"""
File:programming_style.py
-------------------------
"""

# Imperative solution
old_list = [1, 2, 3, 4, 5]
new_list = []

for number in old_list:
    if (number % 2) == 0:
        new_list.append(number)
print(new_list)

# Declarative solution
def is_even(n):
    return (n % 2) == 0

new_list = filter(is_even, [1, 2, 3, 4, 5])

print(new_list)
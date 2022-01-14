"""
File:print_squares.py
---------------------
"""

def print_squares(nums):
    for n in range(len(nums)):
        nums[n] = nums[n] ** 2
    print(nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10]
print(numbers)
print_squares(numbers)
print(numbers)
    
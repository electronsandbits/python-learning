"""
File:get_stats.py
-----------------
Suppose I’m trying to determine various statistics for a population of
alligators. Given a list of lengths, I need to calculate the minimum
and maximum lengths in the population. Here, I do this in a single
function that appears to return two values:
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths) # Two return values

print(f'Min: {minimum}, Max: {maximum}')
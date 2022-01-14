"""
File: get_avg_ratio.py
----------------------
calculates how big each alligator is relative to the population average. This function
returns a list of ratios, but I can receive the longest and shortest
items individually by using a starred expression for the middle portion
of the list:
"""

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)

print(f'Longest:   {longest:>4.0%}')
print(f'Shortest:  {shortest:>4.0%}')
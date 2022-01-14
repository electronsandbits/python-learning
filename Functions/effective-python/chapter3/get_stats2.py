"""
File:get_stats2.py
------------------
Now, imagine that the program’s requirements change, and I need to
also determine the average length, median length, and total population
size of the alligators. I can do this by expanding the get_stats
function to also calculate these statistics and return them in the
result tuple that is unpacked by the caller:
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count # 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    return minimum, maximum, average, median, count
minimum, maximum, average, median, count = get_stats(lengths)

print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count {count}')












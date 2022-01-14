"""
File:higherOrderFunctions.py
----------------------------
"""

def test_numbers_even(numbers):
    results = []
    for n in numbers:
        if n % 2 == 0:
            results.append(True)
    else:
        results.append(False)

    return results

def test_numbers_positive(numbers):
    results = []
    for n in numbers:
        if n > 0:
            results.append(True)
        else:
            results.append(False)

    return results


evens = test_numbers_even([1, 2, 3, 4])
positives = test_numbers_positive([-2, -1, 0, 1, 2])

print(evens)
print(positives)
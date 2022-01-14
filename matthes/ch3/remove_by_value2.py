#
# File:remove_by_value2.py
# ------------------------
# This program demonstrates how to remove an item by value.

motorcycles = ['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

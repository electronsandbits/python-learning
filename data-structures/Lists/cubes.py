"""
File:cubes.py
-------------
This program  prints the cubes of natural numbers.
"""

cubes = [1, 8, 27, 65, 125]
print(cubes)  # [1, 8, 27, 65, 125]
cubes[3] = 64    # the cube of 4 is 64
print(cubes)  # [1, 8, 27, 64, 125]
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(cubes) # [1, 8, 27, 64, 125, 216, 343]
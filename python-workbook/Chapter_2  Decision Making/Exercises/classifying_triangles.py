"""
File:classifying_triangles.py
-----------------------------
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.

@author:electronsandbits
@version:December 14, 2021
"""

a = int(input("Enter the first side:  "))
b = int(input("Enter the second side:  "))
c = int(input("Enter the third side:  "))

if a == b and b == c:
    print("All three lengths are equal, therefore the triangle is an equilateral triangle.")
elif a == b or b == c or a == c:
    print("Two sides are equal, therefore the triangle is an isosceles triangle.")
else:
    print("All three lengths are different, therefore the triangle is scalene .")

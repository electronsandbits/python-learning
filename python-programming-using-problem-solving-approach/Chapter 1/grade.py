"""
grade.py
--------
This program demonstrates an algorithm to
print the grade obtained by a student using the following rule:
----------------------------------------------
Marks                                    Grade
----------------------------------------------
Above  75                                  O
60 - 75                                    A
50 - 60                                    B
40 - 50                                    C
less than 40                               D
-----------------------------------------------

@author: electronsandbits
@version: December 9, 2021
"""
M = int(input("Enter the marks obtained: "))
if M >= 75:
    print("O")
elif M >= 60 d M < 75:
    print("A")
elif M >= 50 and M < 60:
    print("B")
elif M >= 40 and M < 50:
    print("C")
else:
    print("D")



grade = 59
if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")
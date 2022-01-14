"""
File:status.py
--------------
This program demonstrates if expression.
If we wish to decide if someone is a teenager or not
then we might check to see if they are over 12 and under 20
"""

age = int(input("Enter the age: "))
status = None
if (age > 12) and age < 20:
    status = "teenager"
else:
    status = "not teenager"
print(status)

#status = ('teenager' if age > 12 and age < 20 else 'not teenager')
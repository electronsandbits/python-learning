"""
sign_test.py
------------
"""
number = float(input("Enter a number: "))
if number > 0:
  result = "That's a positive number"
elif number < 0:
  result = "That's a negative number"
else:
  result = "That's zero"
print(result)


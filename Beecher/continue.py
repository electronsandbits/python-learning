"""
The following program compares each number in a list to see if it is
greater than, less than, or equal to a test number.
If either of the first two comparisons are successful, all the
following comparisons don’t need to be carried out, so the
computer can jump immediately back to the beginning of the
loop and move onto checking the next number in the list.

file:continue.py
----------------
@author: Frank Funny
@version: Dec 4, 2021
"""

numbers = [12, 72, 48, 24, 14, 28, 17, 29, 7]
test_number = 7

for number in numbers:
    if test_number > number:
       print('Greater than')
       continue

if test_number < number:
    print('Less than')
    continue

if test_number == number:
   print('Equal to')0
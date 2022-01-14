"""
iteration.py
------------
@author: Frank Funny
@version: Dec 4,2021
"""
# This program invites the user to guess a number (set in the
# age variable). As long as they haven’t guessed correctly,
# the program keeps asking.

age = 41
guess = 0

while age != guess:
    # Whereas a == b tests whether a and b are equal, a != b tests
    # whether a and b are not equal
    # The int() function turns the user’s input (which is text) into an integer.
    guess = int(input('Guess how old I am> '))
print('You got it right!')




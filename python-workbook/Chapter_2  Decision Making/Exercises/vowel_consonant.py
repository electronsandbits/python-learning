"""
file:VowelConsonant.py
-----------------------
This program reads a letter of the alphabet from the user.
If the user enters a, e, i, o or u the program should display a message
indicating that the entered letter is a vowel. If the user enters y then the program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise the program should display a message indicating that the
letter is a consonant.

@ author: Frank Funny
@version: December 7, 2021
"""
# Read a letter from the user
letter = input("Enter a letter : ")

# classify the letter and report the result
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("It's a vowel.")
elif letter == "y":
    print("Sometimes it's a vowel ... Sometimes it's a consonant.")
else:
    print("It's  a consonant.")

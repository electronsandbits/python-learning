"""
File: note_to_frequency.py
--------------------------
This program prompts the user to enter an octave of music notes, and
displays the note’s frequency.
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies:

___________________________________
Note                 Frequency (Hz)
-----------------------------------
C4                      261.63
D4                      293.66
E4                      329.63
F4                      349.23
G4                      392.00
A4                      440.00
B4                      493.88
-----------------------------------

Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes
listed  previously.
Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8. While this could be
done by adding many additional cases to your if statement, such a solution is
cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead,
you should exploit the relationship between notes in adjacent octaves. In particular,
the frequency of any note in octave n is half the frequency of the corresponding
note in octave n + 1. By using this relationship, you should be able to
add support for the additional notes without adding additional cases to your if
statement.

Hint: You will want to access the characters in the note entered by the user
individually when completing this exercise. Begin by separating the letter from
the octave. Then compute the frequency for that letter in the fourth octave using
the data in the table above. Once you have this frequency you should divide it
by 2^4−x , where x is the octave number entered by the user. This will halve or
double the frequency the correct number of times.
"""

# Define Constants
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# Prompt the user to enter a musical note
note = input("Enter an octave of music note: ")

# store the note and its octave
musical_note = note[0]
octave = int(note[1])

# Display the corresponding Frequency
if note == "C":
    print("Frequency:", C4)
elif note == "D":
    print("Frequency:", D4)
elif note == "E":
    print("Frequency: ", E4)
elif note == F4:
    print("Frequency:", F4)
elif note == "G":
    print("Frequency: ", G4)
elif note == "A":
    print("Frequency: ", A4)
elif note == "B":
    print("Frequency: ", B4)
else:
    print("Nothing else to show!")

# Adjust the frequency into the correct octave
frequency = frequency / 2 ** (4 - octave)

# Display the result
print("The frequency of ", note, "is", frequency)
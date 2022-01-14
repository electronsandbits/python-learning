"""
The following table lists the sound level in decibels for several common noises.
----------------------------------------
Noise                      Decibel Level
----------------------------------------
Jackhammer                    130 dB
Gas Lawnmower                 106 dB
Alarm Clock                   70 dB
Quiet Room                    40 dB
-----------------------------------------
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.

File:SoundLevels.py
-------------------

@author: electronsandbits
@version: December 14,2021
"""

# Reads in the decibel level from the user
decibel_level = int(input("Enter the Decibel Level:  "))

if decibel_level == 130:
    print("Jackhammer")
elif decibel_level == 106:
    print("Gas Lawnmower ")
elif decibel_level == 70:
    print("Alarm Clock ")
elif decibel_level == 40:
    print("Quiet Room")
elif decibel_level > 130:
    print("Loudest noise ")
elif decibel_level < 40:
    print("quietest noise")
else:
    print("Not listed")
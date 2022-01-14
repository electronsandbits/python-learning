"""
file:name_that_shape.py
-----------------------
This program  determines the name of a shape from its number of sides.It read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. The program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then  the program should display an appropriate error message.

@author:Frank Funny
@version: December 7, 2021
"""
# Read the number of sides from the user
number_of_sides = int(input("Enter the number of sides: "))

# Determine the name, leaving it empty if an unsupported number of sides was entered
name = ""
if number_of_sides == 3:
    name = "triangle"
elif number_of_sides == 4:
    name = "quadrilateral"
elif number_of_sides == 5:
    name = "pentagon"
elif number_of_sides == 6:
    name = "hexagon"
elif number_of_sides == 7:
    name = "heptagon"
elif number_of_sides == 8:
    name = "octagon"
elif number_of_sides == 9:
    name = "nonagon"
elif number_of_sides == 10:
    name = "decagon"

# Display an error message or the name of the polygon
if name == "":
    print("That number of sides is not supported by this program.")
else:
    print("That's a", name)
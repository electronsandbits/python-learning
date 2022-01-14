"""
function:draw_box.py
--------------------
Draw a box outlined with asterisks and filled with spaces.
@param width the width of the box
@param height the height of the box

"""

def draw_box(width, height):
    # A box that is smaller than 2X2 cannot be drawn by this function
    if width < 2 or height < 2:
        print("Error: The width or height is too small.")
        quit()

    # Draw the top of the box
    print("*" * width)

    # Draw the sides of the box
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")

    # Draw the bottom of the box
    print("*" * width)

draw_box(15, 4)
draw_box(1, 1)
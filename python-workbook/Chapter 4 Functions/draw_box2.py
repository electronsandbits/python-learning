"""
function:draw_box2.py
--------------------
Draw a box outlined with asterisks and filled with spaces.
@param width the width of the box
@param height the height of the box
@param outline the character used for the outline of the box
@param fill the character used to fill the box
"""

def draw_box(width, height, outline="*", fill= " "):
    # A box that is smaller than 2X2 cannot be drawn by this function
    if width < 2 or height < 2:
        print("Error: The width or height is too small.")
        quit()

    # Draw the top of the box
    print(outline * width)

    # Draw the sides of the box
    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)

    # Draw the bottom of the box
    print(outline * width)

draw_box(14,  5, "@", ".")
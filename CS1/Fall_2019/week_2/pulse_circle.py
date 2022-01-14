## pulse_circle.py
## A program to demonstrate the use of if statements inside the graphics loop
## Devin Balkcom
## July, 2011
## Modified by THC to use constants and the new cs1lib.

from cs1lib import *

WINDOW_SIZE = 400
WINDOW_CENTER = WINDOW_SIZE // 2

# State variables.
radius = 1      # radius of outermost circle
growing = True  # True if growing, False if shrinking

def pulse_circle():
    global radius, growing

    disable_stroke()

    # Draw the current frame.
    clear()

    set_fill_color(1, 0, 0)  # set the fill color to red
    draw_circle(WINDOW_CENTER, WINDOW_CENTER, radius)

    set_fill_color(0, 0, 1)  # blue
    draw_circle(WINDOW_CENTER, WINDOW_CENTER, radius / 2)

    set_fill_color(1, 1, 0)  # yellow
    draw_circle(WINDOW_CENTER, WINDOW_CENTER, radius / 4)

    # Update the state for the next frame.
    if growing:
        radius = radius + 2
    else:
        radius = radius - 2

    # Need to reverse the direction of growing or shrinking?
    if radius >= WINDOW_CENTER or radius <= 1:
        growing = not growing

start_graphics(pulse_circle, title = "Pulsing Circles", width = WINDOW_SIZE, height = WINDOW_SIZE)

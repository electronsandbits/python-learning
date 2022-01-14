# growing_circle.py
# CS 1 example by Devin Balkcom to animate a circle that grows to fill the window.
# Modified by THC to use constants and for the new cs1lib.

from cs1lib import *

WINDOW_SIZE = 400
WINDOW_CENTER = WINDOW_SIZE // 2

radius = 1  # state variable

def animate_circle():
    global radius

    clear()

    set_fill_color(1, 0, 0)     # red
    draw_circle(WINDOW_CENTER, WINDOW_CENTER, radius)

    # Change the state for the next frame.
    radius = radius + 1
    
start_graphics(animate_circle, title = "Growing Circle",
               width = WINDOW_SIZE, height = WINDOW_SIZE, framerate = 10)
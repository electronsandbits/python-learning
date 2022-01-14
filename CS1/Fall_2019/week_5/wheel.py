# wheel.py
# cs1 class example
#  based on a cs2 example by Fabio Pellacini
#  python version October, 2011, Devin Balkcom
#  Animation by THC.

from cs1lib import *
from math import pi, sin, cos

OUTER_RADIUS = .37  # the relative radius of circles around the outer rim of the wheel
                    # a scaling of .37 causes the circles to just barely touch
                    
OUTER_DISTANCE = 1 - OUTER_RADIUS

FRAME_RATE = 30
TIMESTEP = 1.0 / FRAME_RATE

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

MIN_SIZE = 20       # draw no smaller wheel than this
WHEEL_COUNT = 5     # draw this many wheels in each recursive step
ANGLE_INCREMENT = 360 // WHEEL_COUNT

def radians(degrees):
    return degrees * pi / 180.0

# Compute the x coordinate of a location that is
#  a distance 'distance' from a point cx, cy, with angle
#  'angle' from the horizontal

def compute_polar_x(cx, angle, distance):
    return cx + cos(radians(angle)) * distance
    
def compute_polar_y(cy, angle, distance):
    return cy + sin(radians(angle)) * distance    
    
# Recursively draw the wheels.
def draw_wheel(x, y, r, angle, increment):
    # Draw this wheel.
    set_fill_color(0, 0, 1, .2)
    draw_circle(x, y, r)
    set_fill_color(0, 1, 0, .2)
    draw_circle(x, y, r * (OUTER_DISTANCE - OUTER_RADIUS)) 

    # If this wheel is small enough, we're done.
    if r < MIN_SIZE:
        return

    # Not too small.  Draw the five outer wheels
    for i in range(WHEEL_COUNT):
        new_x = compute_polar_x(x, angle, r * OUTER_DISTANCE)
        new_y = compute_polar_y(y, angle, r * OUTER_DISTANCE)
        
        angle += ANGLE_INCREMENT
    
        draw_wheel(new_x, new_y, r * OUTER_RADIUS, angle + increment, increment)
        draw_line(x, y, new_x, new_y)  # draw the spokes connecting to the outer wheels
    
def main():
    global increment

    set_clear_color(1, 1, 1)
    clear()

    draw_wheel(WINDOW_WIDTH // 2, WINDOW_WIDTH // 2,
               WINDOW_HEIGHT // 2, increment, increment)
    increment += 1

increment = 0

start_graphics(main, title = "The Wheel", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
# hyperspace.py
# By THC.

from random import uniform, randint
from math import pi, sin, cos
from cs1lib import *
from ball import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 600
WINDOW_CENTER_X = WINDOW_WIDTH // 2
WINDOW_CENTER_Y = WINDOW_HEIGHT // 2

# State variables.
ball_list = []  # no balls added yet

# Return a boolean that indicates whether any part of a ball is visible in the window.
def is_visible(ball):
    (left, top, right, bottom) = ball.get_bounding_box()
    return right >= 0 and bottom >= 0 and left < WINDOW_WIDTH and top < WINDOW_HEIGHT

# Remove any ball that is outside the window from the list.
# We loop over the list in reverse, because when an item is removed from the list,
# all of the items after the item have their location in the list reduced by one.
# By looping in reverse, we make sure that the next index the loop looks at
# is the correct one.
def remove_out_of_bounds(moving_balls):
    i = len(moving_balls) - 1
    while i >= 0:
        # If the ball is not visible, remove the ball from the list.
        if not is_visible(moving_balls[i]):
            del moving_balls[i]
        i -= 1

def main():
    set_clear_color(0, 0, 0)
    clear()

    # Draw every ball in the list.
    for ball in ball_list:
        ball.draw()

    r = g = b = 1   # white stars

    new_stars = randint(2, 5)
    for i in range(new_stars):
        # Compute the velocity.  The stars all have the same approximate speed,
        # but random directions.
        speed = randint(5, 8)  # approximate speed in pixels/frame
        angle = uniform(0, 2 * pi)
        x_vel = cos(angle) * speed
        y_vel = sin(angle) * speed
        radius = randint(2, 3)

        new_ball = Ball(WINDOW_CENTER_X, WINDOW_CENTER_Y,
                        x_vel, y_vel, radius, r, g, b)
        ball_list.append(new_ball)

    # Delete any ball from the list that has fallen off the screen.
    remove_out_of_bounds(ball_list)

    # Update the state of every ball in the list.
    for ball in ball_list:
        ball.update_position()

start_graphics(main, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

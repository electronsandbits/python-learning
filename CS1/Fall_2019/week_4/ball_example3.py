# ball_example3.py
# By THC to show updating the Ball's velocity.

from cs1lib import *
from ball import Ball

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

ball = Ball(20, 35, 2, 4, 10, .3, .3, 1.)
h_pressed = False
v_pressed = False

# If the 'q' key is pressed, quit the program.
# Otherwise change state.
def process_key_press(key):
    global h_pressed, v_pressed

    if key == 'h':
        h_pressed = True
    elif key == 'v':
        v_pressed = True
    elif key == 'q':
        cs1_quit()

def main():
    global h_pressed, v_pressed

    set_clear_color(1, 1, 1)
    clear()

    ball.draw()

    # If the 'h' key is pressed, reverse the ball's horizontal direction.
    # If the 'v' key is pressed, reverse the ball's vertical direction.
    if h_pressed:
        ball.reverse_horizontal_direction()
        h_pressed = False
    elif v_pressed:
        ball.reverse_vertical_direction()
        v_pressed = False

    ball.update_position()

start_graphics(main, width = WINDOW_WIDTH, height = WINDOW_HEIGHT,
               key_press = process_key_press)

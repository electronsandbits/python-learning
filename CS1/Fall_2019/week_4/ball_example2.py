from cs1lib import *
from ball import Ball

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

ball = Ball(20, 35, 2, 4, 10, .3, .3, 1.)

def main():
    set_clear_color(1, 1, 1)
    clear()

    ball.draw()

    ball.update_position()

start_graphics(main, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

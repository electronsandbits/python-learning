# ball_example4.py
# By THC.

from random import uniform, randint
from cs1lib import *
from ball import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 600

# State variables.
ball_list = []      # no balls added yet
button_down = False # mouse button is initially up
mouse_x = 0
mouse_y = 0
h_pressed = False
v_pressed = False

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

# If the mouse button is down, record that it's down and its position.
def mouse_down(mx, my):
    global button_down, mouse_x, mouse_y
    button_down = True
    mouse_x = mx
    mouse_y = my

# If the mouse button is up, record that it's up.  Don't care about the position.
def mouse_up(mx, my):
    global button_down
    button_down = False

# If the mouse is moved and the button is down, record its position.
def mouse_drag(mx, my):
    global mouse_x, mouse_y
    if button_down:
        mouse_x = mx
        mouse_y = my

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

    set_clear_color(0, 0, 0)
    clear()
        
    # Draw every ball in the list.
    for ball in ball_list:
        ball.draw()

    # If the mouse button has been pressed, add a new ball with a random
    # radius, color, and velocity.
    if button_down:
        radius = randint(5, 15)
        r = uniform(.5, 1)
        g = uniform(.5, 1)
        b = uniform(.5, 1)

        # Make a random velocity, but not 0 in both dimensions.
        x_vel = 0
        y_vel = 0
        while x_vel == 0 and y_vel == 0:
            x_vel = randint(-6, 6)
            y_vel = randint(-6, 6)

        new_ball = Ball(mouse_x, mouse_y, x_vel, y_vel, radius,
                        r, g, b)
        ball_list.append(new_ball)

    # If the 'h' key is pressed, reverse the horizontal direction for every ball.
    # If the 'v' key is pressed, reverse the vertical direction for every ball.
    if h_pressed:
        for ball in ball_list:
            ball.reverse_horizontal_direction()
        h_pressed = False
    elif v_pressed:
        for ball in ball_list:
            ball.reverse_vertical_direction()
        v_pressed = False

    # Delete any ball from the list that has fallen off the screen.
    remove_out_of_bounds(ball_list)

    # To verify that remove_out_of_bounds works, uncomment the following line.
    # print(len(ball_list))

    # Update the state of every ball in the list.
    for ball in ball_list:
        ball.update_position()

start_graphics(main, height = WINDOW_HEIGHT, width=WINDOW_WIDTH,
               mouse_press = mouse_down, mouse_release = mouse_up,
               mouse_move = mouse_drag, key_press = process_key_press)

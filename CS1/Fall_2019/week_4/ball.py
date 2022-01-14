from cs1lib import *

class Ball:
    # Initialize all the instance variables for this Ball object.
    # Default radius is 10 pixels and default color is gray.
    def __init__(self, start_x_pos, start_y_pos, start_x_vel, start_y_vel,
                 radius = 10, r = 0.5, g = 0.5, b = 0.5):
        # Location, velocities, and size of the ball.
        self.x_pos = start_x_pos
        self.y_pos = start_y_pos
        self.x_vel = start_x_vel
        self.y_vel = start_y_vel
        self.radius = radius

        # Color of the Ball, for drawing.
        self.r = r
        self.g = g
        self.b = b

    # Have the Ball change its position, given a timestep.
    def update_position(self):
        self.x_pos = self.x_pos + self.x_vel
        self.y_pos = self.y_pos + self.y_vel

    # Have the ball reverse its horizontal direction.
    def reverse_horizontal_direction(self):
        self.x_vel = -self.x_vel

    # Have the ball reverse its vertical direction.
    def reverse_vertical_direction(self):
        self.y_vel = -self.y_vel

    # Have the Ball draw itself.
    def draw(self):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x_pos, self.y_pos, self.radius)

    # Return the radius of the Ball.
    def get_radius(self):
        return self.radius

    # Return a 4-tuple of the Ball's left, top, right, and bottom.
    def get_bounding_box(self):
        return (self.x_pos - self.radius,
                self.y_pos - self.radius,
                self.x_pos + self.radius,
                self.y_pos + self.radius)

    # Return a string representing the Ball's position.
    def __str__(self):
        return str(self.x_pos) + ", " + str(self.y_pos)
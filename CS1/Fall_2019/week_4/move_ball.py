from ball import Ball  # import the Ball class

# Create a Ball object and store a reference to it in the variable myball.
myball = Ball(5.0, 4.0, 3.0, 6.0)

print("Ball location " + str(myball.x_pos) + ", " + str(myball.y_pos))

# Move the ball at the current velocity.
myball.update_position()

print("Ball location " + str(myball.x_pos) + ", " + str(myball.y_pos))

# Or use the __str__ method.
print("Ball location", myball)

# Or use the __str__ method again.
print("Ball location " + str(myball))
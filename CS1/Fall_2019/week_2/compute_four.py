from math import sqrt

def compute_four():
    print("Your wish is my command!  I compute four!")
    return 24 // 4 - 2

def calculate_four():
    print("Your wish is my command!  I calculate four!")
    return sqrt(4.0) + 2

def get_me_four():
    return 24 // 4 - 2
    print("I computed the value!")  # this line is "dead code" and never reached

print(compute_four())
print(calculate_four())
print(get_me_four())
from cs1lib import *
from colony import *

hive = Colony(6, 8)  # make a small colony
first_time = True

def main():
    global first_time

    clear()
    hive.draw()

    if first_time:
        # Make a glider by calling flip_cell.
        hive.flip_cell(30, 10)
        hive.flip_cell(50, 30)
        hive.flip_cell(50, 50)
        hive.flip_cell(30, 50)
        hive.flip_cell(10, 50)

        first_time = False
    else:
        hive.compute_generation()

start_graphics(main, framerate = 1)
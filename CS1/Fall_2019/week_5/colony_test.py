from cs1lib import *
from colony import *

hive = Colony(10, 10)
game_on = False

def on_click(mx, my):
    hive.flip_cell(mx, my)

def key_down(key):
    global game_on
    if key == ' ':
        game_on = True
        set_framerate(1)

def main():
    clear()
    hive.draw()

    if game_on:
        hive.compute_generation()

start_graphics(main, mouse_release = on_click, key_press = key_down)
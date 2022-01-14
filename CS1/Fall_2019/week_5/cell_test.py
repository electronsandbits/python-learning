from cs1lib import *
from cell import *

frame_count = 0
c1 = Cell(0, 0)
c2 = Cell(1, 2)

def main():
    global frame_count

    clear()

    if frame_count == 0:
        c1.draw()
        print("Frame " + str(frame_count) + ": " + str(c1))
        set_framerate(0.25)     # now delay 4 seconds between frames
    elif frame_count == 1:
        c1.flip()
        c1.draw()
        print("Frame " + str(frame_count) + ": " + str(c1))
    elif frame_count == 2:
        c1.flip()
        c1.draw()
        print("Frame " + str(frame_count) + ": " + str(c1))
    elif frame_count == 3:
        c1.draw()
        c2.draw()
        print("Frame " + str(frame_count) + ": " + str(c2))
    elif frame_count == 4:
        c1.draw()
        c2.revive()
        c2.draw()
        print("Frame " + str(frame_count) + ": " + str(c2))
    elif frame_count == 5:
        c1.draw()
        c2.kill()
        c2.draw()
        print("Frame " + str(frame_count) + ": " + str(c2))

    frame_count += 1

start_graphics(main)
# sierpinsky.py
# Draws a Sierpinksy Gasket.

from cs1lib import *

GASKET_SIZE = 512

# Draw a Sierpinsky Gasket of width and height d,
# with upper left at (x, y).
def draw_sierpinsky(x, y, d):   
    if d <= 1:
        draw_point(x, y)                        # base case
    else:
        draw_sierpinsky(x, y, d // 2)                   # recurse on upper left quadrant
        draw_sierpinsky(x + d // 2, y, d // 2)          # recurse on upper right quadrant
        draw_sierpinsky(x + d // 2, y + d // 2, d // 2) # recurse on lower right quadrant

def main():
    set_clear_color(0, 0, 0)    # black
    clear()
    set_stroke_color(1, 1, 0)   # yellow
    
    draw_sierpinsky(0, 0, GASKET_SIZE)
    
start_graphics(main, title = "Sierpinsky Gasket", width = GASKET_SIZE, height = GASKET_SIZE)
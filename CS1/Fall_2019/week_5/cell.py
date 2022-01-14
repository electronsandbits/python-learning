# cell.py
# Class for a cell in the Game of Life.

from cs1lib import *

CELL_SIZE = 20      # width and height of each cell, in pixels

class Cell:
    # Initialize a new Cell.
    def __init__(self, row, column):
        self.living = False
        self.row = row
        self.column = column
        
    # Kill this Cell.
    def kill(self):
        self.living = False
        
    # Make this Cell be alive.
    def revive(self):
        self.living = True
        
    # If this Cell is alive, make it dead.
    # If it's dead, make it alive.
    def flip(self):
        self.living = not self.living
        
    # Return whether this Cell is alive.
    def is_living(self):
        return self.living
    
    # Have a Cell draw itself.
    def draw(self):
        enable_stroke()
        set_stroke_color(0, 0, 0)  # black border for all cells

        if self.living:
            set_fill_color(0, 0.75, 1)  # living cells are light blue
        else:
            set_fill_color(1, 1, 0)     # dead cells are yellow

        draw_rectangle(self.column * CELL_SIZE, self.row * CELL_SIZE,
                       CELL_SIZE, CELL_SIZE)

    # Return the string representation of a Cell.
    def __str__(self):
        return "Cell at row " + str(self.row) + " and column " + \
            str(self.column) + " is " + ["dead", "living"][self.living]

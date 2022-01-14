"""
File:neutral_smile_face.py
--------------------------
"""

import tkinter

window = tkinter.Tk()
c = tkinter.Canvas(window)

# Code for drawing objects goes here…
c.pack()
window.mainloop()

def render_neutral_face():
    # Draw face
    c.create_oval(50, 50, 120, 120)

    # Draw eyes
    c.create_oval(60, 60, 80, 80)
    c.create_oval(90, 60, 110, 80)

    # Draw pupils
    c.create_oval(65, 65, 75, 75, fill='black')
    c.create_oval(95, 65, 105, 75, fill='black')

    # Draw mouth
    c.create_line(70, 110, 100, 110)
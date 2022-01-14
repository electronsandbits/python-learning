"""
render_smiley_face.py
---------------------
"""

from tkinter import *
from tkinter import ttk
import tkinter

window = tkinter.Tk()
c = tkinter.Canvas(window)

# Code for drawing objects goes here…
c.pack()
window.mainloop()

def render_smiley_face():
    c.create_oval(50, 50, 120, 120)
    c.create_oval(60, 60, 80, 80)
    c.create_oval(90, 60, 110, 80)
    c.create_oval(65, 65, 75, 75, fill='black')
    c.create_oval(95, 65, 105, 75, fill='black')

    # Draw smiley mouth
    c.create_arc(60, 110, 110, 80, start=0, extent=-180)

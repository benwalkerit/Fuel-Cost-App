#modules
from tkinter import *

        
BACKGROUND_COLOR = "#d3d3d3"

class AppInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Journey Fuel Cost")
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
        self.title_label = Label(text="Journey Fuel Cost", fg="black", bg="BACKGROUND_COLOR")
        
        self.window.mainloop()
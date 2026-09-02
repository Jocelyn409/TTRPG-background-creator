import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import os


# Define frames
class ContactBook(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=16)
        self.pack(fill=BOTH, expand=YES)

        ttk.Label(app).pack(side = "bottom", fill="both", expand = "yes")


# Run app, call frames
if __name__ == "__main__":
    app = ttk.App(title="Background Creator", theme="bootstrap-dark")

    background_image = ImageTk.PhotoImage(Image.open("backgrounds\\night sky.jpeg"))

    ttk.Label(app, image=background_image).pack()

    app.mainloop()
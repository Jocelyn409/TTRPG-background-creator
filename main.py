# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from PIL import Image, ImageTk
# import os


# # Run app, call frames
# if __name__ == "__main__":
#     app = ttk.Window(title="Background Creator", theme="bootstrap-dark")


# # Define frames
# def create_options_window():
#     global options_window

#     options_window = ttk.Toplevel()
#     options_window.title("Options")
#     options_window.geometry("300x400")
#     ttk.Label(options_window, text="Options Window").pack()
#     ttk.Button(options_window, text="Test")


# create_options_window()

# Run app, call frames
# if __name__ == "__main__":
#     app = ttk.Window(title="Background Creator", theme="bootstrap-dark")



import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog

class MainApp(ttk.Window):
    def __init__(self):
        super().__init__(theme="bootstrap-dark")
        self.title("Background Creator")
        self.geometry("1400x800")
        self.bind('<Escape>', self.toggle_fullscreen) # Binds escape key to fullscreen
        self.state = False
        self.sub_window = None
        self.open_sub_window()
        
        ttk.Button(self, text="Choose Background Image", command=self.browse_files, bootstyle=PRIMARY).pack(expand=True)
        

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Toggle boolean
        self.attributes("-fullscreen", self.state)
        self.sub_window.geometry(f"+{self.winfo_x() - self.sub_window.winfo_width() - 10}+{self.winfo_y() + self.winfo_height() // 4}")
        return


    def browse_files(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))


    def open_sub_window(self):
        # Check if window already exists and is open
        if self.sub_window is None or not self.sub_window.winfo_exists():
            self.sub_window = ttk.Toplevel(self) # Keep editor on top level
            self.sub_window.title("Editor")
            self.sub_window.geometry("450x650")
            self.update_idletasks() # idk what this does
            
            ttk.Label(self.sub_window, text="Editor", padding=20).pack()
        else:
            self.sub_window.lift()

        # Always position editor next to main window
        self.sub_window.geometry(f"+{self.winfo_x() - self.sub_window.winfo_width() - 10}+{self.winfo_y() + self.winfo_height() // 4}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
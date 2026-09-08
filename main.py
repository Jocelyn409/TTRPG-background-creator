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




# from screeninfo import get_monitors

# # Get list of all connected monitors
# monitors = get_monitors()

# # Make sure you actually have a second monitor detected
# if len(monitors) > 1:
#     # monitors[0] is primary, monitors[1] is secondary
#     target_monitor = monitors[1] 
# else:
#     target_monitor = monitors[0]

# # Calculate center placement on the target monitor
# win_w, win_h = 800, 600
# x = target_monitor.x + (target_monitor.width - win_w) // 2
# y = target_monitor.y + (target_monitor.height - win_h) // 2

# root.geometry(f"{win_w}x{win_h}+{x}+{y}")



import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Image, filedialog
from PIL import Image, ImageTk

class MainApp(ttk.Window):
    def __init__(self):
        super().__init__(theme="bootstrap-dark")
        self.title("Background Creator")
        self.geometry("1400x800")

        self.state = False
        self.bind('<Escape>', self.toggle_fullscreen) # Binds escape key to fullscreen

        self.sub_window = None
        self.open_sub_window()

        self.file_path = None
        self.background_image = ttk.Label(self).pack()


    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Toggle boolean
        self.attributes("-fullscreen", self.state)
        self.sub_window.geometry(f"+{self.winfo_x() - self.sub_window.winfo_width() - 10}+{self.winfo_y() + self.winfo_height() // 4}")
        return


    # Open file explorer; code from w3resource
    def browse_files(self):
        self.file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
        if self.file_path:
            self.display_image(self.file_path)


    # Display the image chose; code from w3resource
    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.background_image.config(image=photo)
        self.background_image.photo = photo


    def open_sub_window(self):
        # Check if window already exists and is open
        if self.sub_window is None or not self.sub_window.winfo_exists():
            self.sub_window = ttk.Toplevel(self) # Keep editor on top level
            self.sub_window.title("Editor")
            self.sub_window.geometry("450x650")
            self.update_idletasks() # idk what this does tbh
            
            ttk.Label(self.sub_window, text="Editor", padding=20).pack()
            self.sub_window.browse_files_button = ttk.Button(self.sub_window, text="Choose Background Image", command=self.browse_files, bootstyle=PRIMARY).pack(expand=True)
        else:
            self.sub_window.lift()

        # Always position editor next to main window
        self.sub_window.geometry(f"+{self.winfo_x() - self.sub_window.winfo_width() - 10}+{self.winfo_y() + self.winfo_height() // 4}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
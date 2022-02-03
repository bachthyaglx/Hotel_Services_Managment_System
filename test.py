import tkinter as tk
from PIL import ImageTk, Image

def next(panel):
    path = "E:\Thesis\house\hotel_images\girl.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!

def prev(panel):
    path = "E:\Thesis\house\hotel_images\logohotel.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!

#Create main window
window = tk.Tk()

#divide window into two sections. One for image. One for buttons
top = tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

#place image
path = "E:\Thesis\house\hotel_images\logohotel.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.image = img # keep a reference!
panel.pack(side = "top", fill = "both", expand = "yes")


#place buttons
prev_button = tk.Button(window, text="Previous", width=10, height=2, command=lambda: prev(panel))
prev_button.pack(in_=bottom, side="left")
next_button = tk.Button(window, text="Next", width=10, height=2, command=lambda: next(panel))
next_button.pack(in_=bottom, side="right")

#Start the GUI
window.mainloop()
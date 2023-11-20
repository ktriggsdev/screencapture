import time
import numpy as np
import pyscreeze as ss
import tkinter as tk
from PIL import ImageTk, Image


def screenshot():
    name = int(round(time.time() * 1000))
    name = 'screenshots_data/{}.png'.format(name)
    time.sleep(5)
    img = ss.screenshot(name)
    img.show()


root = tk.Tk()
root.configure(bg="#0f0f0f")

# Load the icon image
icon_image = ImageTk.PhotoImage(Image.open('./ss.png'))

# Convert the image to PIL format
image = ImageTk.getimage(icon_image)  # this line might be the issue
array = np.array(image)
pil_image = Image.fromarray(array)

root.iconphoto(True, icon_image)
root.title("Screen Capture Tool")
root.geometry("800x150")


frame = tk.Frame(root)
frame.pack()

ss_img = ImageTk.PhotoImage(Image.open('screenshot.png').resize((50, 50)))
quit_img = ImageTk.PhotoImage(Image.open('quit.png').resize((50, 50)))

button = tk.Button(
    frame,
    image=ss_img,
    bg="black",
    fg="whitesmoke",
    width=400,
    height=150,
    command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    image=quit_img,
    bg="black",
    fg="whitesmoke",
    width=400,
    height=150,
    command=quit)

close.pack(side=tk.LEFT)


root.mainloop()

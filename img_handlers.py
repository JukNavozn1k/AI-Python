import tkinter as tk
from PIL import Image, ImageGrab,ImageTk
import numpy as np 
root = None
canvas = None

def toNumpy():
    global canvas

    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    #image.save("img_source.png")
    # resize to AI input layer
    image = image.resize((28, 28))
    #image.save("img_resized.png")
    img_arr = np.array(image)
    
    return img_arr / 255

def save_img():
    global canvas

    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    image.save("out.png")
   
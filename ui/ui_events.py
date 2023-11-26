
import tkinter as tk
import img_handlers

canvas = None
model = None
label = None 


import numpy as np 

# Функция для рисования 
def paint(event):
    brush_size = 3
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")

def erase(event):
    brush_size = 12
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")

def clear_canvas():
    canvas.delete("all")

def predict():
   arr = 1 -  img_handlers.toNumpy()
   ans = model.model.predict([arr.tolist()],verbose=False)
   label.config(text=f"Я думаю, что это: {np.argmax(ans)}")
   pass
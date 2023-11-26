
import tkinter as tk


canvas = None

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

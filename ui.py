import tkinter as tk
import ui_events


root = tk.Tk()
root.title("MNIST Recognizer 2.0.0!")

canvas = tk.Canvas(root, width=280, height=280, bg="white")
canvas.pack()

ui_events.canvas = canvas

# Mouse binds
canvas.bind("<B1-Motion>", ui_events.paint)
canvas.bind("<B3-Motion>", ui_events.erase)

# Clear Canvas bind
clear_button = tk.Button(root, text="Clear Canvas", command=ui_events.clear_canvas)
clear_button.pack()


# AI Predictor ... 
predict_button = tk.Button(root, text="Predict", command=ui_events.clear_canvas)
predict_button.pack()

root.mainloop()

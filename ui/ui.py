import tkinter as tk
from . import ui_events
import img_handlers

def run(model=None):
    root = tk.Tk()
    root.title("MNIST Recognizer 2.0.0!")

    canvas = tk.Canvas(root, width=280, height=280, bg="white")
    canvas.pack()
    label = tk.Label(root, text="Waiting...", font=("Arial", 12))
    label.pack()

    # Modules init
    ui_events.canvas = canvas
    img_handlers.canvas = canvas
    img_handlers.root = root
    ui_events.model = model
    ui_events.label = label
    
    # Mouse binds
    canvas.bind("<B1-Motion>", ui_events.paint)
    canvas.bind("<B3-Motion>", ui_events.erase)

    # Clear Canvas bind
    clear_button = tk.Button(root, text="Clear Canvas", command=ui_events.clear_canvas)
    clear_button.pack()


    # AI Predictor ... 
    predict_button = tk.Button(root, text="Predict", command=ui_events.predict)
    predict_button.pack()

    
    clear_button = tk.Button(root, text="Save img", command=img_handlers.save_img)
    clear_button.pack()

    root.mainloop()

from tkinter import *
from PIL import ImageGrab
from PIL import Image
import AI
import os
import random
import string
class Paint(Frame):
    def __init__(self, parent):
        AI.learn()
        self.brush_size = 20
        self.brush_color = "black"
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)
    def canc_(self,event):
        self.canv.delete('all')
    def setUI(self):
        self.parent.title("AI Python")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6,weight=1)
        self.rowconfigure(2, weight=1)
        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)
        self.btn = Button(text="Check",padx=514)
        self.btn.bind('<Button-1>', self.check_button)
        self.btn.bind('<Return>', self.check_button)
        self.btn.pack()
        self.number_lab = Label(self, text="Number: ... ")
        self.number_lab.grid(row=0, column=0, padx=6)
        self.canv.bind("<B1-Motion>", self.draw)
        self.canv.bind('<B3-Motion>', self.canc_)
    def check_button(self,event):
        lpx = self.canv.winfo_rootx() + 2
        lpy = self.canv.winfo_rooty() + 2
        rpx = lpx + self.canv.winfo_width() - 4
        rpy = lpy + self.canv.winfo_height() - 4
        file_name = generate_random_string(16)
        img = ImageGrab.grab([lpx, lpy, rpx, rpy]).save(file_name)
        resize(file_name)
        self.number_lab = Label(self, text="Number: "+str(AI.check(file_name)))
        self.number_lab.grid(row=0, column=0, padx=6)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),file_name)
        os.remove(path)


def resize(file_name):
    im = Image.open(file_name)
    h, w = im.size
    scale = 28 / max(h, w)
    im.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS).save(file_name)
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string + '.png'
def main():
    root = Tk()
    root.geometry("514x561+300+300")
    app = Paint(root)
    root.resizable(width=False, height=False)
    root.mainloop()
if __name__ == "__main__":
    main()

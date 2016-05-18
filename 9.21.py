from tkinter import *

class rectangle:
    def __init__(self):
        window= Tk()
        window.title("Inside the rectangle?")

        self.canvas = Canvas(window, height = 100, width = 250, bg = "white")
        self.canvas.pack()
        self.canvas.create_rectangle(50,40,150,80)

        self.canvas.bind("<B1-Motion>", self.isinside)
        self.canvas.focus_set()

        window.mainloop()
    def isinside(self, event):
        if event.x > 50 and event.x < 150:
            if event.y > 40 and event.y <80:
                self.canvas.delete("text")
                self.canvas.create_text(event.x, event.y - 5, text = "Mouse pointer is in the rectangle", tags = "text")
        else:
            self.canvas.delete("text")
            self.canvas.create_text(event.x, event.y - 5, text = "Mouse pointer is not in the rectangle", tags = "text")
rectangle()

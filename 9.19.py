from tkinter import *
from tkinter import ttk

class BouncingBall:
    def __init__(self):
        window = Tk()
        window.title("Bouncing Ball")

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        self.r = 25
        self.x = 100
        self.y = 50
        if self.x == 100 and self.y == 50:
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, tags = "Circle")
        
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()

        

        
        window.mainloop()

    def up(self, event):
        if self.y > 5:
            self.canvas.delete("Circle")
            self.y = (self.y - 5)
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, tags = "Circle")
    def down(self, event):
        if self.y < 75:
            self.canvas.delete("Circle")
            self.y = self.y + 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,  tags = "Circle")
    def left(self, event):
        if self.x > 5:
            self.canvas.delete("Circle")
            self.x = self.x - 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, tags = "Circle")
    def right(self, event):
        if self.x < 175:
            self.canvas.delete("Circle")
            self.x = self.x + 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, tags = "Circle")
BouncingBall()

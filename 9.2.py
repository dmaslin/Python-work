from tkinter import *
from tkinter import ttk

class BouncingBall:
    def __init__(self):
        window = Tk()
        window.title("Bouncing Ball")

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        self.w = IntVar()
        self.r = IntVar()
        self.x = IntVar()
        self.y = IntVar()
        self.w = 3
        self.r = 25
        self.x = 100
        self.y = 50
        if self.x == 100 and self.y == 50:
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,width = self.w, fill = "green", tags = "Circle")

        frame = Frame(window)
        frame.pack()
        
        btUp = Button(frame, text = "Up", command = self.goUp)
        btDown = Button(frame, text = "Down", command = self.goDown)
        btLeft = Button(frame, text = "Left", command = self.goLeft)
        btRight = Button(frame, text = "Right", command = self.goRight)

        btUp.grid(row = 1, column = 1)
        btDown.grid(row = 1, column = 2)
        btLeft.grid(row = 1, column = 3)
        btRight.grid(row = 1, column = 4)

        
        window.mainloop()

    def goUp(self):
        if self.y > 5:
            self.canvas.delete("Circle")
            self.y = (self.y - 5)
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,width = self.w, fill = "green", tags = "Circle")
    def goDown(self):
        if self.y < 75:
            self.canvas.delete("Circle")
            self.y = self.y + 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,width = self.w,fill = "green",  tags = "Circle")
    def goLeft(self):
        if self.x > 5:
            self.canvas.delete("Circle")
            self.x = self.x - 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,width = self.w, fill = "green", tags = "Circle")
    def goRight(self):
        if self.x < 175:
            self.canvas.delete("Circle")
            self.x = self.x + 5
            self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r,width = self.w, fill = "green", tags = "Circle")
BouncingBall()

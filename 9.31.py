from tkinter import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class hiddencircle:
    def __init__(self):
        window = Tk()
        window.title("Dragging the Blue Circle")

        
        self.canvas = Canvas(window, height = 450, width = 600)
        self.canvas.pack()

        self.radius = 50
        self.x = 75
        self.y = 75
        self.blue = Point(self.x, self.y)

        self.canvas.create_oval(self.blue.x, self.blue.y, self.blue.x + 2 * self.radius, self.blue.y + 2 * self.radius, fill = "blue", tags = "bcircle")
        self.canvas.create_oval(self.x + 20 + 2 * self.radius, self.y, self.x + 20 + 4 * self.radius, self.y + 2 * self.radius, fill = "green")
        self.canvas.create_oval(self.x + 40 + 4 * self.radius, self.y, self.x + 40 + 6 * self.radius, self.y + 2 * self.radius, fill = "red")
        self.canvas.create_oval(self.x + self.radius, self.y + self.radius, self.x + 3 * self.radius, self.y + 3 * self.radius, fill = "yellow")
        self.canvas.create_oval(self.x + 20 + 3*self.radius, self.y + self.radius, self.x + 20+ 5 * self.radius, self.y + 3 * self.radius, fill = "orange")

        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.focus_set()

        window.mainloop()
    def move(self,event):
        if ((event.x - (self.x+self.radius))**2 + (event.y - (self.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("bcircle")
            self.blue.x = event.x - self.radius
            self.blue.y = event.y - self.radius
            self.canvas.create_oval(self.blue.x, self.blue.y, self.blue.x + 2 * self.radius, self.blue.y + 2 * self.radius, fill = "blue", tags = "bcircle")    
hiddencircle()

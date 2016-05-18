from tkinter import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class moveTheCircles:
    def __init__(self):
        window = Tk()
        window.title("Olympic Symbol")

        
        self.canvas = Canvas(window, height = 450, width = 600)
        self.canvas.pack()

        self.radius = 50
        self.xb = 75
        self.yb = 75
        self.green = Point(self.xb + 20 + 2 * self.radius, self.yb)
        self.red = Point(self.xb + 40 + 4 * self.radius, self.yb)
        self.yellow = Point(self.xb + self.radius, self.yb + self.radius)
        self.orange = Point(self.xb +20+3*self.radius, self.yb + self.radius)
        self.blue = Point(self.xb, self.yb)

        self.canvas.create_oval(self.blue.x, self.blue.y, self.blue.x + 2 * self.radius, self.blue.y + 2 * self.radius, fill = "blue", tags = "blue")
        self.canvas.create_oval(self.green.x, self.green.y, self.green.x + 2 * self.radius, self.green.y + 2 * self.radius, fill = "green", tags = "green")
        self.canvas.create_oval(self.red.x, self.red.y, self.red.x + 2 * self.radius, self.red.y + 2 * self.radius, fill = "red", tags = "red")
        self.canvas.create_oval(self.yellow.x, self.yellow.y, self.yellow.x + 2 * self.radius, self.yellow.y + 2 * self.radius, fill = "yellow", tags = "yellow")
        self.canvas.create_oval(self.orange.x, self.orange.y, self.orange.x + 2 * self.radius, self.orange.y + 2 * self.radius, fill = "orange", tags = "orange")

        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.focus_set()

        window.mainloop()
    def move(self,event):
        if ((event.x - (self.blue.x+self.radius))**2 + (event.y - (self.blue.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("blue")
            self.blue.x = event.x - self.radius
            self.blue.y = event.y - self.radius
            self.canvas.create_oval(self.blue.x, self.blue.y, self.blue.x + 2 * self.radius, self.blue.y + 2 * self.radius, fill = "blue", tags = "blue")
        elif ((event.x - (self.green.x+self.radius))**2 + (event.y - (self.green.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("green")
            self.green.x = event.x - self.radius
            self.green.y = event.y - self.radius
            self.canvas.create_oval(self.green.x, self.green.y, self.green.x + 2 * self.radius, self.green.y + 2 * self.radius, fill = "green", tags = "green")
        elif ((event.x - (self.red.x+self.radius))**2 + (event.y - (self.red.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("red")
            self.red.x = event.x - self.radius
            self.red.y = event.y - self.radius
            self.canvas.create_oval(self.red.x, self.red.y, self.red.x + 2 * self.radius, self.red.y + 2 * self.radius, fill = "red", tags = "red")
        elif ((event.x - (self.yellow.x+self.radius))**2 + (event.y - (self.yellow.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("yellow")
            self.yellow.x = event.x - self.radius
            self.yellow.y = event.y - self.radius
            self.canvas.create_oval(self.yellow.x, self.yellow.y, self.yellow.x + 2 * self.radius, self.yellow.y + 2 * self.radius, fill = "yellow", tags = "yellow")
        elif ((event.x - (self.orange.x+self.radius))**2 + (event.y - (self.orange.y + self.radius))**2)**.5 < self.radius:
            self.canvas.delete("orange")
            self.orange.x = event.x - self.radius
            self.orange.y = event.y - self.radius
            self.canvas.create_oval(self.orange.x, self.orange.y, self.orange.x + 2 * self.radius, self.orange.y + 2 * self.radius, fill = "orange", tags = "orange")
        
moveTheCircles()

from tkinter import *
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class twolines:
    def __init__(self):
        window = Tk()
        window.title("Intersecting points")
        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(frame, bg = "white")
        self.canvas.pack()
        self.p1 = Point(20,20)
        self.p2 = Point(56,130)
        self.p3 = Point(100, 20)
        self.p4 = Point(16,130)
        self.distancel1 = ((self.p2.x-self.p1.x)**2 + (self.p2.y - self.p1.y)**2)**.5
        self.distancel2 = ((self.p3.y-self.p4.y)**2 + (self.p3.y - self.p4.y)**2)**.5
        self.slopeL1 = [self.p2.y-self.p1.y, self.p2.x-self.p1.x]
        self.slopeL2 = [self.p4.y-self.p3.y, self.p4.x - self.p3.x]
        self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, tags = "line1")
        self.canvas.create_line(self.p3.x, self.p3.y, self.p4.x, self.p4.y, tags = "line2")
        self.canvas.bind("<B1-Motion>", self.moved)
        self.canvas.bind("<ButtonPress-1>", self.press)
        
        self.canvas.focus_set()
        self.intersect()

        window.mainloop()
    def intersect(self):
        a = self.p1.y - self.p2.y
        b = self.p1.x - self.p2.x
        c = a*self.p1.x - self.p1.y * b
        d = self.p3.y - self.p4.y
        e = self.p3.x - self.p4.x
        f = d * self.p3.x - e * self.p3.y
        div = a*e - b*d
        xa = (c*e - b*f) / div
        ya = -1* (a*f - c*d) / div
        if div == 0:
            self.canvas.delete("point")
        elif div != 0:
            self.canvas.delete("point")
            self.canvas.create_oval(xa - 5, ya - 5, xa + 5, ya + 5, fill = "red", tags = "point")
    def press(self, event):
        d1 = ((event.x-self.p1.x)**2 + (event.y - self.p4.y)**2)**.5
        d2 = ((event.x-self.p2.x)**2 + (event.y - self.p4.y)**2)**.5
        d3 = ((event.x-self.p3.x)**2 + (event.y - self.p4.y)**2)**.5
        d4 = ((event.x-self.p4.x)**2 + (event.y - self.p4.y)**2)**.5
        if self.distancel1 - d1 - d2 < 1:
             self.isline1 = True
             self.startx = event.x
             self.starty = event.y 
        if self.distancel2 - d3 - d4 < 1:
            print("yes")
            self.isline2 = True
            self.startx = event.x
            self.starty = event.y
    def moved(self, event):
        if self.isline1 == True:
            dx = event.x - self.startx
            dy = event.y - self.starty
            self.canvas.delete("line1")
            self.p1.x += dx
            self.p1.y += dy
            self.p2.x += dx
            self.p2.y += dy
            self.startx = event.x
            self.starty = event.y
            self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, tags = "line1")
            self.canvas.update()
            self.intersect()
            
        if self.isline2 == True:
            dx = event.x - self.startx
            dy = event.y - self.starty
            self.canvas.move("line2", dx, dy)
            self.p3.x += dx
            self.p3.y += dy
            self.p4.x += dx
            self.p4.y += dy
            self.startx = event.x
            self.starty = event.y
            self.canvas.create_line(self.p3.x, self.p3.y, self.p4.x, self.p4.y, tags = "line2")
            self.intersect()
            self.canvas.update()
twolines()

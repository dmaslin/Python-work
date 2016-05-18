from tkinter import *
import turtle
import math


# Draw a snow flak with the specified order on one line
class KochSnowflake:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Sierpinski Triangle") # Set a title
        
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window, 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
        Label(frame1, 
            text = "Enter an order: ").pack(side = LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable = self.order, 
                      justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display Sierpinski Triangle", 
            command = self.display).pack(side = LEFT)
        self.turtle = turtle.RawTurtle(self.canvas)
        self.turtle.ht()
        self.turtle.speed(0)
        
        
        window.mainloop() # Create an event loop
    def drawLine(self, x1, y1, x2, y2):
        self.turtle.penup()
        self.turtle.goto(x1, y1)
        self.turtle.pendown()
        self.turtle.goto(x2, y2)
        
    def display(self):
        self.turtle.clear()
        p1 = [0, 175]
        p2 = [-150, -75]
        p3 = [150, -75]
        self.displayKochSnowFlake(int(self.order.get()), p1, p2)
        self.displayKochSnowFlake(int(self.order.get()), p2, p3)
        self.displayKochSnowFlake(int(self.order.get()), p3, p1)
        
    
    def displayKochSnowFlake(self, order, p1, p2):
        if order == 0:
            # Draw a line
            self.drawLine(p1[0], p1[1], p2[0], p2[1])
        else:
            # Get points x, y, z on the edge 
            deltaX = p2[0] - p1[0]
            deltaY = p2[1] - p1[1]

            x = [p1[0] + deltaX / 3, p1[1] + deltaY / 3]
            y = [p1[0] + deltaX * 2 / 3, p1[1] + deltaY * 2 / 3]
            z = [((p1[0] + p2[0]) / 2 - math.cos(math.radians(30)) * (p1[1] - p2[1]) / 3),
              (int)((p1[1] + p2[1]) / 2 - math.cos(math.radians(30)) * (p2[0] - p1[0]) / 3)]

            # Recursively display snow flakes on lines
            self.displayKochSnowFlake(order - 1, p1, x)
            self.displayKochSnowFlake(order - 1, x, z)
            self.displayKochSnowFlake(order - 1, z, y)
            self.displayKochSnowFlake(order - 1, y, p2)
        
    # Return the midpoint between two points
    def midpoint(p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p

KochSnowflake()

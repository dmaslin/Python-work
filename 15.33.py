import turtle
from tkinter import *
import math

class hilbert:
    def __init__(self):
        window = Tk()
        window.title("Hilbert Curve")

        self.width = 500
        self.height = 500
        self.canvas = Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()
        
        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
        Label(frame1, 
            text = "Enter an order: ").pack(side = LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable = self.order, 
                      justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display Hilbert Curve", command = self.display).pack(side = LEFT)
        self.turtle = turtle.RawTurtle(self.canvas)
        self.turtle.ht()
        self.turtle.speed(0)

        window.mainloop()

    def display(self):
        self.turtle.clear()

        SIZE = 400
        length = 400

        for i in range(int(self.order.get())):
            length = length / 2 # Get the right length for the order
            
        # Get the start point
        x = -SIZE / 2 + length / 2
        y = SIZE / 2 - length / 2

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

        self.upperU(int(self.order.get()), length)
    def upperU(self, order, length):
        if order > 0:
            self.leftU(order - 1, length)
            self.turtle.setheading(270)
            self.turtle.forward(length)
            self.upperU(order - 1, length)
            self.turtle.setheading(0)
            self.turtle.forward(length)
            self.upperU(order - 1, length)
            self.turtle.setheading(90)
            self.turtle.forward(length)
            self.rightU(order - 1, length)

    def leftU(self, order, length):
        if order > 0:
            self.upperU(order - 1, length)
            self.turtle.setheading(0)
            self.turtle.forward(length)
            self.leftU(order - 1, length)
            self.turtle.setheading(270)
            self.turtle.forward(length)
            self.leftU(order - 1, length)
            self.turtle.setheading(180)
            self.turtle.forward(length)
            self.downU(order - 1, length)

    def rightU(self, order, length):
        if order > 0:
            self.downU(order - 1, length)
            self.turtle.setheading(180)
            self.turtle.forward(length)
            self.rightU(order - 1, length)
            self.turtle.setheading(90)
            self.turtle.forward(length)
            self.rightU(order - 1, length)
            self.turtle.setheading(0)
            self.turtle.forward(length)
            self.upperU(order - 1, length)

    def downU(self, order, length):
        if order > 0:
            self.rightU(order - 1, length)
            self.turtle.setheading(90)
            self.turtle.forward(length)
            self.downU(order - 1, length)
            self.turtle.setheading(180)
            self.turtle.forward(length)
            self.downU(order - 1, length)
            self.turtle.setheading(270)
            self.turtle.forward(length)
            self.leftU(order - 1, length)

hilbert()



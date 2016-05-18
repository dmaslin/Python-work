from tkinter import *
import math

class ytree:
    def __init__(self):
        window = Tk()
        window.title("Recursive Tree")

        self.depth = StringVar()

        self.canvas = Canvas(window, height = 400, width = 400, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Label(frame, text = "Enter the depth: ").pack(side = LEFT)
        Entry(frame, textvariable = self.depth).pack(side = LEFT)
        Button(frame, text = "Show Recursive Tree", command = self.displayYShape).pack(side = LEFT)
        self.x1 = 200
        self.y1 = 250
        self.length = 100
        self.angleFactor = math.pi / 5
        self.sizeFactor = 0.58

        window.mainloop()

    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])

    def displayYShape(self):
        self.displayYShapeHelper(int(self.depth.get()), self.x1, self.y1, self.length, math.pi/2)

    def displayYShapeHelper(self, depth, x1, y1, length, angle):
        if depth >= 0:
            x2 = x1 + math.cos(angle) * length
            y2 = y1 - math.sin(angle) * length

            # Draw the line
            self.drawLine([x1, y1], [x2, y2])

            # Draw the left branch
            self.displayYShapeHelper(depth - 1, x2, y2, length * self.sizeFactor, angle + self.angleFactor)
            # Draw the right branch
            self.displayYShapeHelper(depth - 1, x2, y2, length * self.sizeFactor, angle - self.angleFactor)
        



ytree()

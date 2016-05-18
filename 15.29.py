from tkinter import *

class htree:
    def __init__(self):
        window = Tk()
        window.title("H-Tree")
        self.order = StringVar()

        self.canvas = Canvas(window, height = 400, width = 400, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Label(frame, text = "Enter the order: ").pack(side = LEFT)
        Entry(frame, textvariable = self.order).pack(side = LEFT)
        Button(frame, text = "Show H-Tree", command = self.displayHShape).pack(side = LEFT)
        self.center = [200, 200]
        self.length = 100

        window.mainloop()

    def displayHShape(self):
        self.displayHShapeHelper(int(self.order.get()), self.center, self.length)

    def displayHShapeHelper(self, order, center, length):
        if order >= 0:
            p1 = [center[0] - length / 2, center[1] + length / 2]
            p2 = [center[0] - length / 2, center[1] - length / 2]
            p3 = [center[0] + length / 2, center[1] + length / 2]
            p4 = [center[0] + length / 2, center[1] - length / 2]

            # Draw an H shape
            self.drawLine([center[0] - length / 2, center[1]], 
                [center[0] + length / 2, center[1]])
            self.drawLine(p1, p2)
            self.drawLine(p3, p4)
            
            # Recursively display three H shape of a smaller order
            self.displayHShapeHelper(order - 1, p1, length / 2)
            self.displayHShapeHelper(order - 1, p2, length / 2)
            self.displayHShapeHelper(order - 1, p3, length / 2)
            self.displayHShapeHelper(order - 1, p4, length / 2)
    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])
        

htree()

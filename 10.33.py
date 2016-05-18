from tkinter import *
import random

class histogram:
    def __init__(self):
        window = Tk()
        window.title("Count of Each Letter")
        frame1 = Frame(window)
        frame1.pack()
        self.canvas = Canvas(frame1, height = 320, width = 420, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        Button(frame, text = "Display Histogram", command = self.randomLetters).pack()
        window.mainloop()
    def randomLetters(self):
        self.letters = []
        for i in range(0,1000):
            l = random.randint(97,123)
            self.letters.append(chr(l))
        self.drawGraph()
    def drawGraph(self):
        self.canvas.delete("rectangle")
        self.lettercount = []
        for i in range(97,124):
            self.lettercount.append(self.letters.count(chr(i)))
        top = max(self.lettercount)
        x = 10
        y = 300
        sy = 310
        l = 97
        for i in range(0,26):
            height = (self.lettercount[i] / top)*290
            self.canvas.create_rectangle(x, (y - height), x+ 15, y, tags = "rectangle")
            sx = (x + x + 15)/2
            self.canvas.create_text(sx, sy, text = chr(l + i))
            x += 15
        self.canvas.create_line(10, 300, 410, 300)
        









        
histogram()

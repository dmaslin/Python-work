import math
from tkinter import *

class waves:
    def __init__(self):
        window = Tk()
        window.title("Sine and Cosine Functions")
        width = 400
        height = 150
        frame = Frame(window)
        frame.pack()
        canvas = Canvas(frame, bg = "white", height = 150, width = 400)
        canvas.pack()

        s = []
        for x in range(-175, 176): 
            s.append([x + width / 2, -50 * math.sin((x / 100.0) * 2 * math.pi) + height / 2])
        c = []
        for x in range(-175, 176): 
            c.append([x + width / 2, -50 * math.cos((x / 100.0) * 2 * math.pi) + height / 2])
        for i in range(len(s) - 1):
            canvas.create_line(s[i], s[i + 1])
            canvas.create_line(c[i], c[i+1])
         # Draw X-axis
        canvas.create_line(10, height / 2, width - 10, height / 2)
        canvas.create_text(width / 2 + 100, height / 2 + 10, text = "2\u03c0")
        canvas.create_text(width / 2 - 100, height / 2 + 10, text = "-2\u03c0")
        canvas.create_line(width - 10 -10, height / 2 + 10, width - 10, height / 2)
        canvas.create_line(width - 10 -10, height / 2 - 10, width - 10, height / 2)
        
        # Draw Y-axis
        canvas.create_line(width / 2, 10, width / 2, height - 10)
        canvas.create_line(width / 2, 10, width / 2 - 10, 10 + 10)
        canvas.create_line(width / 2, 10, width / 2 + 10, 10 + 10)
        window.mainloop()
waves()
        

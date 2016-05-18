from tkinter import *
import random
class randomarrow:
    def __init__(self):
        window = Tk()
        window.title("Random an Arrow Line")
        self.canvas = Canvas(window, width = 450, height = 275)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Button(frame, text = "Draw a Random Arrow Line", command = self.rarrow).pack()
        window.mainloop()

    def rarrow(self):
        self.canvas.delete("arrow")
        self.canvas.create_line( random.randint(1,445), random.randint(1,270), random.randint(1,445), random.randint(1,270), arrow = "last", tags = "arrow")
        
randomarrow()

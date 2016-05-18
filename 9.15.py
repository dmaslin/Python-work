from tkinter import *

class stillfan:
    def __init__(self):
        window = Tk()
        window.title("Fan")

        self.canvas = Canvas(height = 500, width = 500, bg = "white")
        self.canvas.pack()

        self.canvas.create_arc(50,50, 450,450, start = 0, extent = 45, fill = "red") 
        self.canvas.create_arc(50,50, 450,450, start = 90, extent = 45, fill = "red")
        self.canvas.create_arc(50,50, 450,450, start = 180, extent = 45, fill = "red")
        self.canvas.create_arc(50,50, 450,450, start = 270, extent = 45, fill = "red")

        window.mainloop()
stillfan()

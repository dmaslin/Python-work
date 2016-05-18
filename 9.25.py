from tkinter import *

class traffic:
    def __init__(self):
        window = Tk()
        window.title("Traffic Lights")
        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(frame, height = 300, width = 300, bg = "white")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()

        self.canvas.create_rectangle(100, 5, 200, 285)
        self.red = self.canvas.create_oval(100,5, 200, 95, tags = "red")
        self.yellow = self.canvas.create_oval(100, 100, 200, 190, tags = "yellow")
        self.green = self.canvas.create_oval(100, 195, 200, 285, tags = "green")

        self.v1 = StringVar()

        Radiobutton(frame, text = "red", variable = self.v1, value = 'R', command = self.lightChange).pack(side = LEFT)
        Radiobutton(frame, text = "yellow", variable = self.v1, value = 'Y', command = self.lightChange).pack(side = LEFT)
        Radiobutton(frame, text = "green", variable = self.v1, value = 'G', command = self.lightChange).pack(side = LEFT)

        window.mainloop()
    def lightChange(self):
        if self.v1.get() == 'R':
            self.canvas.itemconfigure(self.red, fill = "red")
            self.canvas.itemconfigure(self.yellow, fill = "white")
            self.canvas.itemconfigure(self.green, fill = "white")
        elif self.v1.get() == 'Y':
            self.canvas.itemconfigure(self.red, fill = "white")
            self.canvas.itemconfigure(self.yellow, fill = "yellow")
            self.canvas.itemconfigure(self.green, fill = "white")
        elif self.v1.get() == 'G':
            self.canvas.itemconfigure(self.red, fill = "white")
            self.canvas.itemconfigure(self.yellow, fill = "white")
            self.canvas.itemconfigure(self.green, fill = "green")

        
traffic()

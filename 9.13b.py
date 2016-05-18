from tkinter import *

class coordtwo:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")

        self.canvas = Canvas(window, bg = "white", width = 200, height = 100)
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.processMouseEvent1)
        self.canvas.bind("<ButtonRelease-1>", self.processMouseEvent2)
        self.canvas.focus_set()
        window.mainloop()
    def processMouseEvent1(self, event):
        self.text = event.x,",",event.y
        self.canvas.create_text(event.x, event.y, text = self.text, tags = "pos")
    def processMouseEvent2(self, event):
        self.canvas.delete("pos")
coordtwo()

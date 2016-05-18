from tkinter import *

class coordone:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")

        self.canvas = Canvas(window, bg = "white", width = 200, height = 100)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.processMouseEvent)
        self.canvas.focus_set()
        window.mainloop()
    def processMouseEvent(self, event):
        self.canvas.delete("pos")
        self.text = event.x,",",event.y
        self.canvas.create_text(event.x, event.y, text = self.text, tags = "pos")
coordone()

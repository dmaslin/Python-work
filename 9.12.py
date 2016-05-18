from tkinter import *
class FlipFlop:
    def __init__(self):
        window = Tk()
        window.title("Rotating Message")


        self.canvas = Canvas(window, height = 250, width = 300, bg = "white")
        self.canvas.pack()

        self.string = "Programming is fun"
        self.v1 = 1

        self.text = self.canvas.create_text(125, 150, text = self.string, tags = "message")
        self.canvas.bind("<Button-1>", self.processMouseEvent)

        self.canvas.focus_set()

        window.mainloop()


    def processMouseEvent(self, event):
        if self.string == "Programming is fun":
            self.string = "It is fun to program"
            self.canvas.itemconfigure(self.text, text = self.string)
            self.v1 = 1
        elif self.string != "Programming is fun":
            self.string = "Programming is fun"
            self.canvas.itemconfigure(self.text, text = self.string)
            self.v1 = 1
FlipFlop()

from tkinter import *

class rbandmoving:
    def __init__(self):
        window= Tk()
        window.title("Radio buttons and buttons")

        frame1 = Frame(window)
        frame1.pack()
        frame2 = Frame(window)
        frame2.pack()
        self.canvas = Canvas(frame2, height = 50, width = 300)
        self.canvas.pack()
        frame3 = Frame(window)
        frame3.pack()
        self.x = 150
        self.canvas.create_text(self.x,25, text = "Welcome", tags = "text")
        self.v1 = StringVar()
        rbRed = Radiobutton(frame1, text = "red", variable = self.v1, value = 'R', command = self.processRadiobutton).pack(side = LEFT)
        rbYellow = Radiobutton(frame1, text = "yellow", variable = self.v1, value = 'Y', command = self.processRadiobutton).pack(side = LEFT)
        rbWhite = Radiobutton(frame1, text = "white", variable = self.v1, value = 'W', command = self.processRadiobutton).pack(side = LEFT)
        rbGrey = Radiobutton(frame1, text = "grey", variable = self.v1, value = 'G', command = self.processRadiobutton).pack(side = LEFT)
        rbGreen = Radiobutton(frame1, text = "green", variable = self.v1, value = 'E', command = self.processRadiobutton).pack(side = LEFT)

        leftImage = PhotoImage(file = "pybook/image/left.gif")
        rightImage = PhotoImage(file = "pybook/image/right.gif")
        Button(frame3, image = leftImage, command = self.left).pack(side = LEFT)
        Button(frame3, image = rightImage, command = self.right).pack(side = LEFT)

        window.mainloop()

    def left(self):
        self.canvas.move("text", -20, 0)
        self.canvas.update()
    def right(self):
        self.canvas.move("text", 20, 0)
        self.canvas.update()
    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.canvas["bg"] = "red"
        elif self.v1.get() == 'Y':
            self.canvas["bg"] = "yellow"
        elif self.v1.get() == 'W':
            self.canvas["bg"] = "white"
        elif self.v1.get() == 'G':
            self.canvas["bg"] = "grey"
        elif self.v1.get() == 'E':
            self.canvas["bg"] = "green"
        
        

rbandmoving()

from tkinter import *
import random

class trippleT:
    def __init__(self):
        window = Tk()
        window.title("Tic-Tac-Toe")

        frame1 = Frame(window)
        frame1.pack()
        self.crossImage = PhotoImage(file = "cross.gif")
        self.circleImage = PhotoImage(file = "circle.gif")
        self.lbl = []
        for i in range(3):
            self.lbl.append([])
            for j in range(3):
                x = random.randint(1,2)
                if x == 1:
                    self.lbl[i].append(Label(frame1, image = self.crossImage))
                    self.lbl[i][j].grid(row = i +1, column = j+1)
                elif x == 2:
                    self.lbl[i].append(Label(frame1, image = self.circleImage))
                    self.lbl[i][j].grid(row = i +1, column = j+1)
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, text = "Refresh", command = self.refresh).pack()
        window.mainloop()

    def refresh(self):
        for i in range(3):
            for j in range(3):
                x = random.randint(1,2)
                if x == 1:
                    self.lbl[i][j].configure(image = self.crossImage)
                elif x == 2:
                    self.lbl[i][j].configure(image = self.circleImage)

trippleT()

from tkinter import *
import random

class trippleT:
    def __init__(self):
        window = Tk()
        window.title("Tic-Tac-Toe")

        self.frame1 = Frame(window)
        self.frame1.pack()
        self.crossImage = PhotoImage(file = "cross.gif")
        self.circleImage = PhotoImage(file = "circle.gif")
        self.box = PhotoImage(file = "empty.gif")
        self.btn = []
        self.btn.append(Button(self.frame1, image = self.box, command = self.change1))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change2))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change3))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change4))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change5))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change6))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change7))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change8))
        self.btn.append(Button(self.frame1, image = self.box, command = self.change9))
        self.x = []
        self.o = []
        for r in range(3):
            self.x.append([])
            self.o.append([])
            for c in range(3):
                self.x[r].append(False)
                self.o[r].append(False)
        for i in range(3):
            for j in range(3):
                self.btn[(i*3)+j].grid(row = i +1, column = j+1)
        frame2 = Frame(window)
        frame2.pack()
        self.banner = Label(frame2, text ="X please make your selection")
        self.banner.pack()
        self.counter = 0
        window.mainloop()

    def change1(self):
        if self.counter%2 == 0:
            self.btn[0] = Label(self.frame1, image = self.crossImage)
            self.btn[0].grid(row = 1, column = 1)
            self.x[0][0] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[0] = Label(self.frame1, image = self.circleImage)
            self.btn[0].grid(row = 1, column = 1)
            self.o[0][0] = True
            self.check(self.o)
    def change2(self):
        if self.counter%2 == 0:
            self.btn[1] = Label(self.frame1, image = self.crossImage)
            self.btn[1].grid(row = 1, column = 1)
            self.x[0][1] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[1] = Label(self.frame1, image = self.circleImage)
            self.btn[1].grid(row = 1, column = 2)
            self.o[0][1] = True
            self.check(self.o)
    def change3(self):
        if self.counter%2 == 0:
            self.btn[0] = Label(self.frame1, image = self.crossImage)
            self.btn[0].grid(row = 1, column = 3)
            self.x[0][2] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[2] = Label(self.frame1, image = self.circleImage)
            self.btn[2].grid(row = 1, column = 3)
            self.o[0][2] = True
            self.check(self.o)
    def change4(self):
        if self.counter%2 == 0:
            self.btn[3] = Label(self.frame1, image = self.crossImage)
            self.btn[3].grid(row = 2, column = 1)
            self.x[1][0] = True
            self.check(x)
        elif self.counter%2 == 1:
            self.btn[3] = Label(self.frame1, image = self.circleImage)
            self.btn[3].grid(row = 2, column = 1)
            self.o[1][0] = True
            self.check(self.o)
    def change5(self):
        if self.counter%2 == 0:
            self.btn[4] = Label(self.frame1, image = self.crossImage)
            self.btn[4].grid(row = 2, column = 2)
            self.x[1][1] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[4] = Label(self.frame1, image = self.circleImage)
            self.btn[4].grid(row = 2, column = 2)
            self.o[1][1] = True
            self.check(self.o)
    def change6(self):
        if self.counter%2 == 0:
            self.btn[5] = Label(self.frame1, image = self.crossImage)
            self.btn[5].grid(row = 2, column = 3)
            self.x[1][2] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[5] = Label(self.frame1, image = self.circleImage)
            self.btn[5].grid(row = 2, column = 3)
            self.o[1][2] = True
            self.check(self.o)
    def change7(self):
        if self.counter%2 == 0:
            self.btn[6] = Label(self.frame1, image = self.crossImage)
            self.btn[6].grid(row = 3, column = 1)
            self.x[2][0] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[6] = Label(self.frame1, image = self.circleImage)
            self.btn[6].grid(row = 3, column = 1)
            self.o[2][0] = True
            self.check(self.o)
    def change8(self):
        if self.counter%2 == 0:
            self.btn[7] = Label(self.frame1, image = self.crossImage)
            self.btn[7].grid(row = 3, column = 2)
            self.x[2][1] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[7] = Label(self.frame1, image = self.circleImage)
            self.btn[7].grid(row = 3, column = 2)
            self.o[2][1] = True
            self.check(self.o)
    def change9(self):
        if self.counter%2 == 0:
            self.btn[8] = Label(self.frame1, image = self.crossImage)
            self.btn[8].grid(row = 3, column = 3)
            self.x[2][2] = True
            self.check(self.x)
        elif self.counter%2 == 1:
            self.btn[8] = Label(self.frame1, image = self.circleImage)
            self.btn[8].grid(row = 3, column = 3)
            self.o[2][2] = True
            self.check(self.o)
    def check(self, s):
        if self.counter%2 == 0:
            if s[0][0] == True and s[1][1] == True and s[2][2] == True:
                self.victoryx()
            elif s[0][2] == True and s[1][1] == True and s[2][0] == True:
                self.victoryx()
            elif s[0][0] == True and s[0][1] == True and s[0][2] == True:
                self.victoryx()
            elif s[1][0] == True and s[1][1] == True and s[1][2] == True:
                self.victoryx()
            elif s[2][0] == True and s[2][1] == True and s[2][2] == True:
                self.victoryx()
            elif s[0][0] == True and s[1][0] == True and s[2][0] == True:
                self.victoryx()
            elif s[0][1] == True and s[1][1] == True and s[2][1] == True:
                self.victoryx()
            elif s[0][2] == True and s[1][2] == True and s[2][2] == True:
                self.victoryx()
            else:
                self.counter +=1
                if self.counter < 8:
                    self.nextTurn()
                else:
                    self.draw()
        elif self.counter%2 == 1:
            if s[0][0] == True and s[1][1] == True and s[2][2] == True:
                self.victoryo()
            elif s[0][2] == True and s[1][1] == True and s[2][0] == True:
                self.victoryo()
            elif s[0][0] == True and s[0][1] == True and s[0][2] == True:
                self.victoryo()
            elif s[1][0] == True and s[1][1] == True and s[1][2] == True:
                self.victoryo()
            elif s[2][0] == True and s[2][1] == True and s[2][2] == True:
                self.victoryo()
            elif s[0][0] == True and s[1][0] == True and s[2][0] == True:
                self.victoryo()
            elif s[0][1] == True and s[1][1] == True and s[2][1] == True:
                self.victoryo()
            elif s[0][2] == True and s[1][2] == True and s[2][2] == True:
                self.victoryo()
            else:
                self.counter +=1
                if self.counter < 8:
                    self.nextTurn()
                else:
                    self.draw()
    def nextTurn(self):
        if self.counter%2 == 0:
            self.banner["text"] = "X please make your selection"
        elif self.counter%2 == 1:
            self.banner["text"] = "O please make your selection"
    def victoryx(self):
        self.banner["text"] = "X won! The game is over"
    def victoryo(self):
        self.banner["text"] = "O won! The game is over"
    def draw(self):
        self.banner["text"] = "Draw! The game is over"
trippleT()

from tkinter import *
import tkinter.messagebox
class conFour:
    def __init__(self):
        window = Tk()
        window.title("Connect Four")
        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(frame, height = 220, width = 220)
        self.canvas.pack()

        self.rx = 1.0
        self.ry = 1.0
        self.size = 30
        self.cx = 6
        self.cy = 6
        self.radius = 20

        self.circle = []
        self.rectangle = []
        self.r = []
        self.y = []
        self.taken= []
        for r in range(6):
            self.r.append([])
            self.y.append([])
            self.taken.append([])
            for c in range(6):
                self.r[r].append(False)
                self.y[r].append(False)
                self.taken[r].append(False)
        for i in range(6):
            self.circle.append([])
            self.rectangle.append([])
            for c in range(6):
                self.rectangle[i].append(self.canvas.create_rectangle(self.rx, self.ry, (self.rx + self.size), (self.ry + self.size), fill = "purple"))
                self.rx += 35
                
                self.circle[i].append(self.canvas.create_oval(self.cx, self.cy, self.cx + self.radius, self.cy + self.radius, fill = "white"))
                self.cx += 35
            self.rx = 1
            self.ry += 35
            self.cx = 5
            self.cy += 35
        self.counter = 0
        self.column = [1, 36, 71, 106, 141, 176]
        self.canvas.bind("<Button-1>", self.change)
        self.canvas.focus_set()

        Button(frame, text = "Start Over", command = self.restart).pack()
        

        window.mainloop()
    def change(self, event):
        if self.counter%2 == 0:
            if event.x >= self.column[0] and event.x <= self.column[0]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][0] == False:
                        self.canvas.itemconfig(self.circle[row][0], fill = "red")
                        self.taken[row][0] = True
                        self.r[row][0] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[1] and event.x <= self.column[1]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][1] == False:
                        self.canvas.itemconfig(self.circle[row][1], fill = "red")
                        self.taken[row][1] = True
                        self.r[row][1] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[2] and event.x <= self.column[2]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][2] == False:
                        self.canvas.itemconfig(self.circle[row][2], fill = "red")
                        self.taken[row][2] = True
                        self.r[row][2] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[3] and event.x <= self.column[3]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][3] == False:
                        self.canvas.itemconfig(self.circle[row][3], fill = "red")
                        self.taken[row][3] = True
                        self.r[row][3] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[4] and event.x <= self.column[4]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][4] == False:
                        self.canvas.itemconfig(self.circle[row][4], fill = "red")
                        self.taken[row][4] = True
                        self.r[row][4] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[5] and event.x <= self.column[5]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][5] == False:
                        self.canvas.itemconfig(self.circle[row][5], fill = "red")
                        self.taken[row][5] = True
                        self.r[row][5] = True
                        self.check(self.r)
                        self.counter += 1
                        return
                    else:
                        row -= 1
        elif self.counter %2 == 1:
            if event.x >= self.column[0] and event.x <= self.column[0]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][0] == False:
                        self.canvas.itemconfig(self.circle[row][0], fill = "yellow")
                        self.taken[row][0] = True
                        self.y[row][0] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[1] and event.x <= self.column[1]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][1] == False:
                        self.canvas.itemconfig(self.circle[row][1], fill = "yellow")
                        self.taken[row][1] = True
                        self.y[row][1] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[2] and event.x <= self.column[2]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][2] == False:
                        self.canvas.itemconfig(self.circle[row][2], fill = "yellow")
                        self.taken[row][2] = True
                        self.y[row][2] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[3] and event.x <= self.column[3]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][3] == False:
                        self.canvas.itemconfig(self.circle[row][3], fill = "yellow")
                        self.taken[row][3] = True
                        self.y[row][3] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[4] and event.x <= self.column[4]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][4] == False:
                        self.canvas.itemconfig(self.circle[row][4], fill = "yellow")
                        self.taken[row][4] = True
                        self.y[row][4] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
            elif event.x >= self.column[5] and event.x <= self.column[5]+self.size:
                row = 5
                while row > -1:
                    if self.taken[row][5] == False:
                        self.canvas.itemconfig(self.circle[row][5], fill = "yellow")
                        self.taken[row][5] = True
                        self.y[row][5] = True
                        self.check(self.y)
                        self.counter += 1
                        return
                    else:
                        row -= 1
    def check(self, values):
        for row in range(len(values)):
            for column in range(len(values[0])):
                if row <= (len(values) - 4) and column <= (len(values[0])-4):
                    if values[row][column] == True and values[row][column] == values[row + 1][column + 1]  and values[row+1][column +1 ] == values[row + 2][column + 2]  and values[row+2][column + 2] == values[row+3][column + 3]:
                        self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+1][column+1], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+2][column+2], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+3][column+3], fill = "white")
                        tkinter.messagebox.showinfo("Congulations", "A player has won")
                    elif values[row][column] == True and values[row][column] == values[row][column +1] and values[row][column+1] == values[row][column +2] and values[row][column+2] == values[row][column +3]:
                        self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row][column+1], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row][column+2], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row][column+3], fill = "white")
                        tkinter.messagebox.showinfo("Congulations", "A player has won")
                    if values[row][column] == True and values[row][column] == values[row+1][column]  and values[row+1][column] == values[row+2][column]  and values[row+2][column] == values[row+3][column]:
                        self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+1][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+2][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+3][column], fill = "white")
                        tkinter.messagebox.showinfo("Congulations", "A player has won")
                elif row <= (len(values) - 4):
                    if values[row][column] == True and values[row][column] == values[row+1][column]  and values[row+1][column] == values[row+2][column]  and values[row+2][column] == values[row+3][column]:
                        self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+1][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+2][column], fill = "white")
                        self.canvas.itemconfig(self.rectangle[row+3][column], fill = "white")
                        tkinter.messagebox.showinfo("Congulations", "A player has won")
                elif row >= (len(values) - 4) and column <= (len(values[0]) - 4):
                        if values[row][column] == True and values[row][column] == values[row][column +1] and values[row][column+1] == values[row][column +2] and values[row][column+2] == values[row][column +3]:
                            self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row][column+1], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row][column+2], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row][column+3], fill = "white")
                            tkinter.messagebox.showinfo("Congulations", "A player has won")
                        elif values[row][column] == True and values[row][column] == values[row - 1][column + 1]  and values[row-1][column +1 ] == values[row - 2][column + 2]  and values[row-2][column + 2] == values[row-3][column + 3]:
                            self.canvas.itemconfig(self.rectangle[row][column], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row-1][column+1], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row-2][column+2], fill = "white")
                            self.canvas.itemconfig(self.rectangle[row-3][column+3], fill = "white")
                            tkinter.messagebox.showinfo("Congulations", "A player has won")
        return
    def restart(self):
        self.rx = 1
        self.ry = 1
        self.size = 30
        self.cx = 6
        self.cy = 6
        self.radius = 20
        for i in range(6):
            for j in range(6):
                self.r[i][j] = False
                self.y[i][j] = False
                self.taken[i][j] =False
                self.rectangle[i][j] = self.canvas.create_rectangle(self.rx, self.ry, self.rx + self.size, self.ry + self.size, fill = "purple")
                self.circle[i][j] = self.canvas.create_oval(self.cx, self.cy, self.cx + self.radius, self.cy + self.radius, fill = "white" )
                self.rx += 35
                self.cx += 35
            self.rx = 1
            self.cx = 5
            self.ry += 35
            self.cy += 35
        self.counter = 0
conFour()
            

        

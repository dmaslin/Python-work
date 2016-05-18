from tkinter import*
class conFour:
    def __init__(self):
        window = Tk()
        window.title("Consecutive Four")
        frame = Frame(window)
        frame.pack()

        self.values = []
        for i in range(6):
            self.values.append([])
            for j in range(7):
                self.values[i].append(StringVar())
        self.e = []
        for i in range(6):
            self.e.append([])
            for j in range(7):
                self.e[i].append(Entry(frame, width = 2, justify = RIGHT, textvariable = self.values[i][j]))
                self.e[i][j].grid(row = i, column = j)

        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text = "Solve", command = self.isConsecutiveFour).pack()
        window.mainloop()
    def isConsecutiveFour(self):
        for row in range(len(self.values)):
            for column in range(len(self.values[0])):
                if row <= (len(self.values) - 4) and column <= (len(self.values[0])-4):
                    if self.values[row][column].get() == self.values[row + 1][column + 1].get()  and self.values[row+1][column +1 ].get() == values[row + 2][column + 2].get()  and self.values[row+2][column + 2].get() == self.values[row+3][column + 3].get():
                        x1, x2, x3, x4, y1, y2, y3, y4 = row, row +1, row +2, row + 3, column, column + 1, column + 2, column +3
                        self.e[x1][y1].configure(bg = "red")
                        self.e[x1][y1].update()
                        self.e[x2][y2].configure(bg = "red")
                        self.e[x2][y2].update()
                        self.e[x3][y3].configure(bg = "red")
                        self.e[x3][y3].update()
                        self.e[x4][y4].configure(bg = "red")
                        self.e[x4][y4].update()
                    elif self.values[row][column].get() == self.values[row][column +1].get() and self.values[row][column+1].get() == self.values[row][column +2].get() and self.values[row][column+2].get() == self.values[row][column +3].get():
                        x1, x2, x3, x4, y1, y2, y3, y4 = row, row, row, row, column, column + 1, column + 2, column +3
                        self.e[x1][y1].configure(bg = "red")
                        self.e[x1][y1].update()
                        self.e[x2][y2].configure(bg = "red")
                        self.e[x2][y2].update()
                        self.e[x3][y3].configure(bg = "red")
                        self.e[x3][y3].update()
                        self.e[x4][y4].configure(bg = "red")
                        self.e[x4][y4].update()
                    elif self.values[row][column].get() == self.values[row+1][column].get()  and self.values[row+1][column].get() == self.values[row+2][column].get()  and self.values[row+2][column].get() == self.values[row+3][column].get():
                        x1, x2, x3, x4, y1, y2, y3, y4 = row, row +1, row +2, row + 3, column, column, column, column
                        self.e[x1][y1].configure(bg = "red")
                        self.e[x1][y1].update()
                        self.e[x2][y2].configure(bg = "red")
                        self.e[x2][y2].update()
                        self.e[x3][y3].configure(bg = "red")
                        self.e[x3][y3].update()
                        self.e[x4][y4].configure(bg = "red")
                        self.e[x4][y4].update()
                elif row <= (len(self.values) - 4):
                    if self.values[row][column].get() == self.values[row+1][column].get()  and self.values[row+1][column].get() == self.values[row+2][column].get()  and self.values[row+2][column].get() == self.values[row+3][column].get():
                        x1, x2, x3, x4, y1, y2, y3, y4 = row, row +1, row +2, row + 3, column, column , column , column
                        self.e[x1][y1].configure(bg = "red")
                        self.e[x1][y1].update()
                        self.e[x2][y2].configure(bg = "red")
                        self.e[x2][y2].update()
                        self.e[x3][y3].configure(bg = "red")
                        self.e[x3][y3].update()
                        self.e[x4][y4].configure(bg = "red")
                        self.e[x4][y4].update()
                elif row >= (len(self.values) - 4) and column <= (len(self.values[0]) - 4):
                        if self.values[row][column].get() == self.values[row][column +1].get() and self.values[row][column+1].get() == self.values[row][column +2].get() and self.values[row][column+2].get() == self.values[row][column +3].get():
                            x1, x2, x3, x4, y1, y2, y3, y4 = row, row, row, row, column, column + 1, column + 2, column +3
                            self.e[x1][y1].configure(bg = "red")
                            self.e[x1][y1].update()
                            self.e[x2][y2].configure(bg = "red")
                            self.e[x2][y2].update()
                            self.e[x3][y3].configure(bg = "red")
                            self.e[x3][y3].update()
                            self.e[x4][y4].configure(bg = "red")
                            self.e[x4][y4].update()
                        elif self.values[row][column].get() == self.values[row - 1][column + 1].get()  and self.values[row-1][column +1 ].get() == self.values[row - 2][column + 2].get()  and self.values[row-2][column + 2].get() == self.values[row-3][column + 3].get():
                            x1, x2, x3, x4, y1, y2, y3, y4 = row, row -1, row -2, row - 3, column, column + 1, column + 2, column +3
                            self.e[x1][y1].configure(bg = "red")
                            self.e[x1][y1].update()
                            self.e[x2][y2].configure(bg = "red")
                            self.e[x2][y2].update()
                            self.e[x3][y3].configure(bg = "red")
                            self.e[x3][y3].update()
                            self.e[x4][y4].configure(bg = "red")
                            self.e[x4][y4].update()
conFour()

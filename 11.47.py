from tkinter import *
import random

class largeBlock:
    def __init__(self):
        window = Tk()
        window.title("Find Largest Block")
        frame = Frame(window)
        frame.pack()
        frame2 = Frame(window)
        frame2.pack()

        self.v = []
        for i in range(10):
            self.v.append([])
            for j in range(10):
                self.v[i].append(IntVar())
        self.e = []
        for r in range(10):
            self.e.append([])
            for c in range(10):
                x = random.randint(0,1)
                self.v[r][c].set(x)
                self.e[r].append(Entry(frame, width = 2, justify = RIGHT, textvariable = self.v[r][c]))
                self.e[r][c].grid(row = r, column = c)
        Button(frame2, text = "Refresh", command = self.refresh).pack(side = LEFT)
        Button(frame2, text = "Find Largest Block", command = self.large).pack(side = LEFT)
        window.mainloop()

    def refresh(self):
        self.v = []
        for i in range(10):
            self.v.append([])
            for j in range(10):
                self.v[i].append(IntVar())
                self.v[i][j].set(random.randint(0,1))
        for r in range(10):
            for c in range(10):
                self.e[r][c].configure(bg = "white")
                self.e[r][c].delete(0, END)
                self.e[r][c].insert(0, self.v[r][c].get())
    def large(self):
        counter = 10
        while counter > 0:#this will count down in block size finding the largest one its first and ending the loop
            for i in range(10 - counter +1):
                for j in range(10 - counter + 1):
                    num = 0
                    numb = 0
                    for k in range(0, counter):
                        if self.v[i][j+k].get() == 0:
                            num +=1
                        elif self.v[i][j+k].get() == 1:
                            numb  += 1
                if num == counter:
                    print(i)
                    print(j)
                    for x in range(1, counter):
                        for y in range(0, counter):
                            if self.v[i+x][j+y].get() == 0:
                                num +=1
                    if num == counter * counter :
                        self.show(i, j, counter)
                        return
                        
                elif numb == counter:
                    for x in range(1, counter):
                        for y in range(0, counter):
                            if self.v[i+x][j+y].get() == 1:
                                numb +=1
                    if numb == counter * counter :
                        self.show(i, j, counter)
                        return
            counter -= 1
    def show(self, i, j, counter):
        for r in range(counter):
            for c in range(counter):
                self.e[i+r][j+c].configure(bg = "red")
                self.e[i+r][j+c].update()
            
        
largeBlock()

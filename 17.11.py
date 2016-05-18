from tkinter import *
import tkinter.messagebox
import random
class QuickSort:
    def __init__(self):
        self.lst = []

        for i in range(20):
            self.lst.append(random.randint(1,999))
        window = Tk()
        window.title("Quick Sort")
        self.first = 0
        self.last = len(self.lst) -  1
        self.canvas = Canvas(window, height = 170, width = 820)
        self.canvas.pack()
        self.x = 10
        self.y = 80
        self.low = self.first +1
        self.high = self.last
        self.pivot = self.lst[self.first]
        self.oldLow = self.low
        self.oldHigh = self.high
        self.oldPivot = self.lst.index(self.pivot)
        self.px = 30
        self.py = 70
        self.hx = 790
        self.hy = 70
        self.lx = 70
        self.ly = 70
        self.canvas.create_line(self.px, self.py, self.px, self.py - 20, arrow = FIRST, tags = "pivot")
        self.canvas.create_text(self.px, self.py - 30, text = "Pivot", tags = "pivot")
        self.canvas.create_line(self.lx, self.ly, self.lx, self.ly - 20, arrow = FIRST, tags = "low")
        self.canvas.create_text(self.lx, self.ly - 30, text = "Low", tags = "low")
        self.canvas.create_line(self.hx, self.hy, self.hx, self.hy - 20, arrow = FIRST, tags = "high")
        self.canvas.create_text(self.hx, self.hy - 30, text = "High", tags = "high")
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20, tags = "rectangle")
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
        frame = Frame(window)
        frame.pack()
        Button(frame, text = "Step", command = self.quickSortHelper).pack(side = LEFT)
        Button(frame, text = "Reset", command = self.reset).pack(side = LEFT)
        window.mainloop()
    def reset(self):
        self.canvas.delete(ALL)
        
        self.lst = []

        for i in range(20):
            self.lst.append(random.randint(1,999))
        self.first = 0
        self.last = len(self.lst) -  1
        self.low = self.first +1
        self.high = self.last
        self.pivot = self.lst[self.first]
        self.oldLow = self.low
        self.oldHigh = self.high
        self.oldPivot = self.lst.index(self.pivot)
        self.px = 30
        self.py = 70
        self.hx = 790
        self.hy = 70
        self.lx = 70
        self.ly = 70
        self.canvas.create_line(self.px, self.py, self.px, self.py - 20, arrow = FIRST, tags = "pivot")
        self.canvas.create_text(self.px, self.py - 30, text = "Pivot", tags = "pivot")
        self.canvas.create_line(self.lx, self.ly, self.lx, self.ly - 20, arrow = FIRST, tags = "low")
        self.canvas.create_text(self.lx, self.ly - 30, text = "Low", tags = "low")
        self.canvas.create_line(self.hx, self.hy, self.hx, self.hy - 20, arrow = FIRST, tags = "high")
        self.canvas.create_text(self.hx, self.hy - 30, text = "High", tags = "high")
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20, tags = "rectangle")
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
    def check(self):
        check = True
        for i in range(1, len(self.lst)):
            if self.lst[i-1] > self.lst[i]:
                check = False
        return check

    def quickSortHelper(self):
        if not self.check():
            self.pIndex = -1
            self.pIndex = self.partition()
            self.first = 0
            self.last = self.pIndex - 1
            self.high = self.last
            self.low = self.first + 1
            self.pivot = self.lst[self.first]
            self.partition()
            firstHalf = True
            self.first = self.pIndex + 1
            self.last = len(self.lst) - 1
            self.high = self.last
            self.low = self.first + 1
            self.pivot = self.lst[self.first]
            self.partition()
        else:
            tkinter.messagebox.showinfo("Done", "The list has been sorted")
            return
    def checkLow(self):
        if self.low <= self.high and self.lst[self.low] <= self.pivot:
            x = self.lst[self.low]
            self.lst.pop(self.low)
            self.lst.insert(0, x)
            self.low += 1
            self.update()
            return True

    def checkHigh(self):
        if self.low <= self.high and self.lst[self.high] > self.pivot:
            y = self.lst[self.high]
            self.lst.pop(self.high)
            self.lst.insert(len(self.lst) - 1, y)
            self.high -= 1
            self.update()
            return True

    def lowVsHigh(self):
        if self.lst[self.low] >= self.lst[self.high]:
             self.lst[self.high], self.lst[self.low] = self.lst[self.low], self.lst[self.high]
             self.update()
             return True
            
    # Partition list[first..last] 
    def partition(self):
        if self.high > self.low:
            if self.checkLow():
                return

            # Search backward from right
            if self.checkHigh():
                return
            # Swap two elements in the list
            if self.lowVsHigh():
                return

        # Swap pivot with list[high]
        if self.pivot > self.lst[self.high] and self.high < self.low:
            self.lst[self.first] = self.lst[self.high]
            self.lst[self.high] = self.pivot
            return self.high
        else:
            return self.first
    def update(self):
        self.canvas.delete(ALL)
        if self.oldPivot != self.lst.index(self.pivot):
            self.px += 40
            self.oldPivot = self.lst.index(self.pivot)

            
        if self.oldLow != self.low:
            self.lx += 40
            self.oldLow = self.low
        if self.oldHigh != self.high:
            self.hx -= 40
            self.oldHigh = self.high
        self.canvas.create_line(self.px, self.py, self.px, self.py - 20, arrow = FIRST, tags = "pivot")
        self.canvas.create_text(self.px, self.py - 30, text = "Pivot", tags = "pivot")
        self.canvas.create_line(self.lx, self.ly, self.lx, self.ly - 20, arrow = FIRST, tags = "low")
        self.canvas.create_text(self.lx, self.ly - 30, text = "Low", tags = "low")
        self.canvas.create_line(self.hx, self.hy, self.hx, self.hy - 20, arrow = FIRST, tags = "high")
        self.canvas.create_text(self.hx, self.hy - 30, text = "High", tags = "high")
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20, tags = "rectangle")
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
QuickSort()

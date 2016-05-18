from tkinter import *
import random as r
import tkinter.messagebox

class animatedRadix:
    def __init__(self):
        self.lst = []
        self.bucket = []
        for i in range(10):
            self.bucket.append([])
        for i in range(20):
            self.lst.append(r.randint(0,1000))

        window = Tk()
        window.title("Radix Sort")

        self.canvas = Canvas(window, width = 820, height = 170)
        self.canvas.pack()
        self.x = 10
        self.y = 10
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20, tags = "rectangle")
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
        self.bx = 20
        self.by = 45
        for i in range(10):
            self.canvas.create_rectangle(self.bx, self.by, self.bx + 60, self.by + 100)# bucket rectangles
            self.bx += 70
            self.canvas.create_text(self.x + 40 + (i * 70), 160, text = "bucket["+str(i)+"]")
        self.bx = 20
        
        frame = Frame(window)
        frame.pack()
        self.complete = False
        self.tmp = -1
        self.placement  = 1
        self.counter = 0
        self.bucketCounter = 0
        m = max(self.lst)
        m = list(str(m))
        self.maxKey = len(m)
        print(self.maxKey)
        self.key = 1

        Button(frame, text = "Step", command = self.step).pack(side = LEFT)
        Button(frame, text = "Reset", command = self.reset).pack(side = LEFT)
        window.mainloop()
    def updateBucket(self):
        for i in range(len(self.bucket)):
            for j in range(len(self.bucket[i])):
                self.canvas.create_text(self.bx + 30, self.by + 10, text = str(self.bucket[i][j]), tags = "bucket")
                self.canvas.update()
                self.by += 10
            self.bx += 70
            self.by = 45
        self.bx = 20
        self.by = 45
    def lstUpdate(self):
        
        self.canvas.delete(ALL)
        self.bucket = []
        for i in range(10):
            self.bucket.append([])
        self.x = 10
        self.y = 10
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20)
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
        self.bx = 20
        self.by = 45
        for i in range(10):
            self.canvas.create_rectangle(self.bx, self.by, self.bx + 60, self.by + 100)# bucket rectangles
            self.bx += 70
            self.canvas.create_text(self.x + 40 + (i * 70), 160, text = "bucket["+str(i)+"]")
        self.bx = 20
        self.canvas.update()

    def step(self):
        #checks to see that self.lst isn't sorted by seeing that key isn't greater than the max key
        if self.key <= self.maxKey:
            #checks if all of the elements in self.lst have been ordered
            if self.counter + 1 != len(self.lst):
                self.bucketCounter = 0
                self.canvas.delete(str(self.counter))
                self.canvas.update()
                a = str(self.lst[self.counter])
                a = list(a)
                if len(a) >= self.key:
                    lastDigit = eval(a[len(a) - self.key])
                else:
                    lastDigit = 0
                self.bucket[lastDigit].append(self.lst[self.counter])
                self.counter += 1
                self.updateBucket()
            else:
                self.canvas.delete("bucket")
                for i in range(10):
                    for j in range(len(self.bucket[i])):
                        self.lst[self.bucketCounter] = self.bucket[i][j]
                        self.bucketCounter += 1
                self.key +=1
                self.counter = 0
                self.lstUpdate()
        else:
            tkinter.messagebox.showinfo("Done", "The list has been sorted please press restart")
                
            

    def reset(self):
        self.canvas.delete(ALL)
        self.lst = []
        self.bucket = []
        for i in range(10):
            self.bucket.append([])
        for i in range(20):
            self.lst.append(r.randint(0,1000))
        self.x = 10
        self.y = 10
        for i in range(20):
            self.canvas.create_rectangle(self.x + (i*40), self.y, self.x + 40 + (i*40), self.y + 20)
            self.canvas.create_text(self.x + 20 + (i*40), self.y + 10, text = self.lst[i], tags = str(i))
        self.bx = 20
        self.by = 45
        for i in range(10):
            self.canvas.create_rectangle(self.bx, self.by, self.bx + 60, self.by + 100)# bucket rectangles
            self.bx += 70
            self.canvas.create_text(self.x + 40 + (i * 70), 160, text = "bucket["+str(i)+"]")
        self.bx = 20
        self.complete = False
        self.tmp = -1
        self.placement  = 1
        self.counter = 0
        self.bucketCounter = 0
        m = max(self.lst)
        m = list(str(m))
        self.maxKey = len(m)
        print(self.maxKey)
        self.key = 1
        self.canvas.update()
        










            
animatedRadix()

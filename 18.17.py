from tkinter import *
from Queue import Queue
import tkinter.messagebox
class animatedLinkedList:
    def __init__(self):
        window = Tk()
        window.title("Linked List")

        self.lst = Queue()

        self.canvas = Canvas(window, width = 400, height = 200)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Label(frame, text = "Element").pack(side = LEFT)
        self.v1 = StringVar()
        self.v1.set("")
        Entry(frame, textvariable = self.v1).pack(side = LEFT)
        self.lstx = 10
        self.lsty = 80
        self.bx = 10
        self.by = 100
        
        Button(frame, text = "Insert (enqueue)", command = self.insert).pack(side = LEFT)
        Button(frame, text = "Delete (dequeue)", command = self.delete).pack(side = LEFT)
        window.mainloop()
    def insert(self):
        if self.v1.get() == "":
            tkinter.messagebox.showerror("Error", "No input in element")
        else:
            self.lst.enqueue(int(self.v1.get()))
            self.update()
    def delete(self):
        self.lst.dequeue()
        self.update()
    def update(self):
        self.canvas.delete(ALL)
        x = self.lst.getSize()
        self.lstx = 10
        self.lsty = 80
        self.n = self.lst.__str__()
        self.n = self.n.split(", ")
        if len(self.n) > 1:
            a = self.n[0]
            self.n[0] = a.replace("[", "")
            b = self.n[len(self.n) - 1]
            self.n[len(self.n) - 1] = b.replace("]", "")
        elif len(self.n) == 1:
            a = self.n[0]
            a = a.replace("[", "")
            a = a.replace("]", "")
            self.n[0] = a
        print(self.n)
        
        for i in range(x):
            self.canvas.create_rectangle(self.lstx, self.lsty, self.lstx + 30, self.lsty + 20)
            self.canvas.create_text(self.lstx + 15, self.lsty + 10, text = self.n[i])
            self.lstx += 30
animatedLinkedList()

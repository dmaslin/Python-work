from tkinter import *
from linkedlist3 import LinkedList
import tkinter.messagebox
class animatedLinkedList:
    def __init__(self):
        window = Tk()
        window.title("Linked List")

        self.lst = LinkedList()

        self.canvas = Canvas(window, width = 400, height = 200)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Label(frame, text = "Element").pack(side = LEFT)
        self.v1 = StringVar()
        self.v1.set("")
        Entry(frame, textvariable = self.v1).pack(side = LEFT)
        Label(frame, text = "Index").pack(side = LEFT)
        self.v2 = StringVar()
        self.v2.set("")
        Entry(frame, textvariable = self.v2, width = 3).pack(side = LEFT)
        self.n = iter(self.lst)
        self.lstx = 10
        self.lsty = 80
        self.bx = 10
        self.by = 100
        
        Button(frame, text = "Search", command = self.search).pack(side = LEFT)
        Button(frame, text = "Insert", command = self.insert).pack(side = LEFT)
        Button(frame, text = "Delete", command = self.delete).pack(side = LEFT)
        window.mainloop()

    def search(self):
        if self.v1.get() == "":
            tkinter.messagebox.showerror("Error", "No input in element")
        else:
            if self.lst.contains(eval(self.v1.get())):
                tkinter.messagebox.showinfo("Correct", self.v1.get()+" is in the Linked List")
            else:
                tkinter.messagebox.showinfo("Sorry", self.v1.get()+" is not in the Linked List")
    def insert(self):
        if self.v2.get() == "":
            if self.v1.get() == "":
                tkinter.messagebox.showerror("Error", "No input in element")
            else:
                self.lst.add(int(self.v1.get()))
                self.update()
        else:
            if self.v1.get() == "":
                tkinter.messagebox.showerror("Error", "No input in element")
            else:
                self.lst.insert(int(self.v2.get()), int(self.v1.get()))
                self.update()
    def delete(self):
        if self.lst.contains(int(self.v1.get())):
            m = [int(self.v1.get())]
            self.lst.removeAll(m)
            self.update()
        elif self.v1.get() == "":
            tkinter.messagebox.showerror("Error", "No input in element")
    def update(self):
        self.canvas.delete(ALL)
        x = self.lst.getSize()
        self.n = iter(self.lst)
        self.lstx = 10
        self.lsty = 80
        self.bx = 10
        self.by = 100
        if x > 1:
            self.canvas.create_text(10, 10, text = "head")
            self.canvas.create_line(15, 15, 15, 80, fill = "red", arrow = LAST)
            for i in range(x):
                self.canvas.create_rectangle(self.lstx, self.lsty, self.lstx + 30, self.lsty + 20)
                self.canvas.create_rectangle(self.bx, self.by, self.bx + 30, self.by + 20)
                self.canvas.create_text(self.lstx + 15, self.lsty + 10, text = str(next(self.n)))
                self.canvas.create_text(self.bx + 15, self.by + 10, text = "NEXT")
                self.lstx += 50
                self.bx += 50
                if i < x - 1:
                    self.canvas.create_line(self.bx-20, self.by+20, self.bx, self.lsty, fill = "red", arrow = LAST)

            self.canvas.create_text(self.lstx, self.lsty - 20, text = "Tail")
            self.canvas.create_line(self.lstx, self.lsty - 15, self.lstx -20, self.lsty, fill = "red", arrow = LAST)
        else:
            self.canvas.create_text(10, 10, text = "head")
            self.canvas.create_line(15, 15, 15, 80, fill = "red", arrow = LAST)
            self.canvas.create_text(self.lstx, self.lsty - 20, text = "Tail")
            self.canvas.create_line(self.lstx, self.lsty - 15, self.lstx + 30, self.lsty, fill = "red", arrow = LAST)
            self.canvas.create_rectangle(self.lstx, self.lsty, self.lstx + 30, self.lsty + 20)
            self.canvas.create_rectangle(self.bx, self.by, self.bx + 30, self.by + 20)
            self.canvas.create_text(self.lstx + 15, self.lsty + 10, text = str(next(self.n)))
            self.canvas.create_text(self.bx + 15, self.by + 10, text = "NEXT")
animatedLinkedList()

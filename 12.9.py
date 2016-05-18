from tkinter import *

class tworect:
    def __init__(self):
        window = Tk()
        window.title("Two Rectangles")

        frame1 = Frame(window)
        frame1.pack()
        frame2 = Frame(window)
        frame2.pack()
        frame3 = Frame(window)
        frame3.pack()
        frame4 = Frame(window)
        frame4.pack()

        self.banner = Label(frame1, text = "Two rectangles")
        self.banner.pack()
        
        self.canvas = Canvas(frame2, height = 150, width = 300, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.focus_set()

        self.r = []
        for x in range(2):
            self.r.append([])
            for y in range(4):
                self.r[x].append(DoubleVar())
                self.r[x][y].set(self.r[x][y])

        Label(frame3, text = "R1 Center x: ").grid(row = 1, column = 1)
        Entry(frame3, width = 4,justify = RIGHT, textvariable = self.r[0][0]).grid(row = 1, column = 2)
        Label(frame3, text = "R2 Center x: ").grid(row = 1, column = 3)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[1][0]).grid(row = 1, column = 4)
        Label(frame3, text = "R1 Center y: ").grid(row = 2, column = 1)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[0][1]).grid(row = 2, column = 2)
        Label(frame3, text = "R2 Center y: ").grid(row = 2, column = 3)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[1][1]).grid(row = 2, column = 4)
        Label(frame3, text = "R1 Width: ").grid(row = 3, column = 1)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[0][2]).grid(row = 3, column = 2)
        Label(frame3, text = "R2 Width: ").grid(row = 3, column = 3)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[1][2]).grid(row = 3, column = 4)
        Label(frame3, text = "R1 Height: ").grid(row = 4, column = 1)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[0][3]).grid(row = 4, column = 2)
        Label(frame3, text = "R2 Height: ").grid(row = 4, column = 3)
        Entry(frame3, width = 4, justify = RIGHT, textvariable = self.r[1][3]).grid(row = 4, column = 4)

        Button(frame4, text = "Redraw Rectangles", command = self.redraw).pack()

    def move(self, event):
        if event.x >= self.x1 and event.x <= self.x1 + self.r[0][2].get():
            if event.y >= self.y1 and event.y <= self.y1 + self.r[0][3].get():
                self.canvas.delete("r1")
                self.r[0][0].set(event.x)
                self.r[0][1].set(event.y)
                self.x1 = self.r[0][0].get() - (self.r[0][2].get() / 2)
                self.y1 = self.r[0][1].get() - (self.r[0][3].get() / 2)
                
                self.canvas.create_rectangle(self.x1, self.y1, self.r[0][2].get() + self.x1, self.r[0][3].get() + self.y1, tags = "r1")
                self.canvas.create_text(self.r[0][0].get(), self.r[0][1].get(), text = "R1", tags = "r1")
                self.canvas.update()
                self.check()
        elif event.x >= self.x2 and event.x <= self.x2 + self.r[1][2].get():
            if event.y >= self.y2 and event.y <= self.y2 + self.r[1][3].get():
                self.canvas.delete("r2")
                self.r[1][0].set(event.x)
                self.r[1][1].set(event.y)
                self.x2 = self.r[1][0].get() - (self.r[1][2].get() / 2)
                self.y2 = self.r[1][1].get() - (self.r[1][3].get() / 2)
                
                self.canvas.create_rectangle(self.x2,self.y2, self.r[1][2].get() + self.x2, self.r[1][3].get() + self.y2, tags = "r2")
                self.canvas.create_text(self.r[1][0].get(), self.r[1][1].get(), text = "R2", tags = "r2")
                self.canvas.update()
                self.check()

    def redraw(self):
        self.x1 = self.r[0][0].get() - (self.r[0][2].get() / 2)
        self.y1 = self.r[0][1].get() - (self.r[0][3].get() / 2)

        self.x2 = self.r[1][0].get() - (self.r[1][2].get() / 2)
        self.y2 = self.r[1][1].get() - (self.r[1][3].get() / 2)

        self.canvas.create_rectangle(self.x2,self.y2, self.r[1][2].get() + self.x2, self.r[1][3].get() + self.y2, tags = "r2")
        self.canvas.create_text(self.r[1][0].get(), self.r[1][1].get(), text = "R2", tags = "r2")

        self.canvas.create_rectangle(self.x1, self.y1, self.r[0][2].get() + self.x1, self.r[0][3].get() + self.y1, tags = "r1")
        self.canvas.create_text(self.r[0][0].get(), self.r[0][1].get(), text = "R1", tags = "r1")

        self.check()
    def check(self):
        r1c1x = self.x1
        r1c1y = self.y1
        r1c2x = self.x1 + self.r[0][2].get()
        r1c2y = self.y1
        r1c3x = self.x1
        r1c3y = self.y1 + self.r[0][3].get()
        r1c4x = self.x1 + self.r[0][2].get()
        r1c4y = self.y1 + self.r[0][3].get()
        r2c1x = self.x2
        r2c1y = self.y2
        r2c2x = self.x2 + self.r[1][2].get()
        r2c2y = self.y2
        r2c3x = self.x2
        r2c3y = self.y2 + self.r[1][3].get()
        r2c4x = self.x2 + self.r[1][2].get()
        r2c4y = self.y2 + self.r[1][3].get()
        if (r1c1x >= self.x2 and r1c1x <= r2c2x) and (r1c1y >= self.y2 and r1c1y <= r2c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r1c2x >= self.x2 and r1c2x <= r2c2x) and (r1c2y >= self.y2 and r1c2y <= r2c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r1c3x >= self.x2 and r1c3x <= r2c2x) and (r1c3y >= self.y2 and r1c3y <= r2c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r1c4x >= self.x2 and r1c4x <= r2c2x) and (r1c4y >= self.y2 and r1c4y <= r2c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r2c1x >= self.x1 and r2c1x <= r1c2x) and(r2c1y >= self.y2 and r2c1y <= r1c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r2c2x >= self.x1 and r2c2x <= r1c2x) and(r2c2y >= self.y2 and r2c2y <= r1c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r2c3x >= self.x1 and r2c3x <= r1c3x) and(r2c3y >= self.y2 and r2c3y <= r1c3y):
            self.banner["text"] = "Two rectangles intersect"
        elif (r2c4x >= self.x1 and r2c4x <= r1c2x) and(r2c4y >= self.y2 and r2c4y <= r1c3y):
            self.banner["text"] = "Two rectangles intersect"
        else:
            self.banner["text"] = "Two rectangles do not intersect"

        
tworect()

from tkinter import *

class twoRectangles:
    def __init__(self):
        window = Tk()
        window.title("Two Rectangles")
        self.frame = Frame(window)
        self.frame.pack()
        self.banner = Label(self.frame, text = "Two rectangles don't intersect")
        self.banner.pack()

        self.canvas = Canvas(self.frame, height = 150, width = 300)
        self.canvas.pack()

        self.x2 = 75
        self.y2 = 10
        self.x1 = 30
        self.y1 = 30
        self.r2side = 30
        self.r1height = 50
        
        self.canvas.create_rectangle(self.x2,self.y2, self.r2side + self.x2, self.r2side + self.y2, tags = "r2")
        self.canvas.create_text(self.x2 + (self.r2side/2), self.y2 + (self.r2side/2), text = "R2", tags = "r2")

        self.canvas.create_rectangle(self.x1, self.y1, self.r2side + self.x1, self.r1height + self.y1, tags = "r1")
        self.canvas.create_text(self.x1 + (self.r2side/2), self.y1 + (self.r1height/2), text = "R1", tags = "r1")
        self.canvas.bind("<B1-Motion>", self.overlap)
        self.canvas.focus_set()

        window.mainloop()
    def overlap(self, event):
        if event.x >= self.x1 and event.x <= self.x1 + self.r2side:
            if event.y >= self.y1 and event.y <= self.y1 + self.r1height:
                self.canvas.delete("r1")
                self.x1 = event.x - 10
                self.y1 = event.y - 20
                self.canvas.create_rectangle(self.x1, self.y1, self.r2side + self.x1, self.r1height + self.y1, tags = "r1")
                self.canvas.create_text(self.x1 + (self.r2side/2), self.y1 + (self.r1height/2), text = "R1", tags = "r1")
                self.canvas.update()
        elif event.x >= self.x2 and event.x <= self.x2 + self.r2side:
            if event.y >= self.y2 and event.y <= self.y2 + self.r2side:
                self.canvas.delete("r2")
                self.x2 = event.x - 10
                self.y2 = event.y - 10
                self.canvas.create_rectangle(self.x2,self.y2, self.r2side + self.x2, self.r2side + self.y2, tags = "r2")
                self.canvas.create_text(self.x2 + (self.r2side/2), self.y2 + (self.r2side/2), text = "R2", tags = "r2")
                self.canvas.update()
        if self.x2 >= self.x1 and self.x2 <= self.x1 + self.r2side:
            if self.y2 >= self.y1 and self.y2 <= self.y1 + self.r1height:
                self.banner["text"] = "Two rectangles intersect"
            else:
                self.banner["text"] = "Two rectangles do not intersect"
        elif self.x1 >= self.x2 and self.x1 <= self.x2 + self.r2side:
            if self.y1 >= self.y2 and self.y1 <= self.y2 + self.r2side:
                self.banner["text"] = "Two rectangles intersect"
            else:
                self.banner["text"] = "Two rectangles do not intersect"
        else:
            self.banner["text"] = "Two rectangles do not intersect"
                
        




        
twoRectangles()

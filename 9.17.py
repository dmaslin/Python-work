from tkinter import *

class racecar:
    def __init__(self):
        window = Tk()
        window.title("Racing Car")

        self.canvas = Canvas(window, height = 100, width = 300, bg = "white")
        self.canvas.pack()
        self.x = 10
        self.y = 90

        self.canvas.create_oval(self.x+20,self.y - 10, self.x + 30, self.y, fill = "red", tags = "car")
        self.canvas.create_oval(self.x+40,self.y - 10, self.x +50, self.y, fill = "red", tags = "car")
        self.canvas.create_rectangle(self.x+10, self.y -20, self.x+60, self.y -10, fill = "yellow", tags = "car")
        self.canvas.create_polygon(self.x+30,self.y-30, self.x+40,self.y-30, self.x+50,self.y-20,self.x+20,self.y-20, fill = "Orange", tags = "car")

        self.canvas.bind("<Up>", self.faster)
        self.canvas.bind("<Down>", self.slower)
        self.canvas.focus_set()
        self.dx = 10
        self.offset = 100
        self.animate()
        window.mainloop()
    def animate(self):        
        while True:
            self.canvas.move("car",self.dx,0)
            self.canvas.after(self.offset)
            self.canvas.update()
            if self.x < 240:
                self.x += self.dx
            else:
                self.x = 10
                self.canvas.delete("car")
                self.canvas.create_oval(self.x+20,self.y - 10, self.x + 30, self.y, fill = "red", tags = "car")
                self.canvas.create_oval(self.x+40,self.y - 10, self.x +50, self.y, fill = "red", tags = "car")
                self.canvas.create_rectangle(self.x+10, self.y -20, self.x+60, self.y -10, fill = "yellow", tags = "car")
                self.canvas.create_polygon(self.x+30,self.y-30, self.x+40,self.y-30, self.x+50,self.y-20,self.x+20,self.y-20, fill = "Orange", tags = "car")
                
    def faster(self, event):
        if self.offset > 5:
            self.offset -=20
    def slower(self, event):
        self.offset +=20
        
racecar()

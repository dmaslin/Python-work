from tkinter import *

class swirl:
    def __init__(self):
        window = Tk()
        window.title("Arrow Keys")

        self.canvas = Canvas(window, bg = "white", width = 400, height = 200)
        self.canvas.pack()

        self.x = 200
        self.y = 100
        self.deviation = 10

        self.direction = "up"

        self.canvas.bind("<Up>", self.processUp)
        self.canvas.bind("<Down>", self.processDown)
        self.canvas.bind("<Left>", self.processLeft)
        self.canvas.bind("<Right>", self.processRight)
        self.canvas.focus_set()

        self.animate()
        window.mainloop()
        
    def animate(self):
        while True: 
            if self.direction == "up":
                self.canvas.create_line(self.x, self.y, self.x, (self.y - self.deviation))
                self.y -= self.deviation 
                self.canvas.after(500)
                self.canvas.update()
            elif self.direction == "down":
                self.canvas.create_line(self.x, self.y, self.x, (self.y + self.deviation))
                self.y += self.deviation 
                self.canvas.after(500)
                self.canvas.update()
            elif self.direction == "left":
                self.canvas.create_line(self.x, self.y, self.x - self.deviation, self.y)
                self.x -= self.deviation 
                self.canvas.after(500)
                self.canvas.update()
            elif self.direction == "right":
                self.canvas.create_line(self.x, self.y, self.x + self.deviation, self.y)
                self.x += self.deviation 
                self.canvas.after(500)
                self.canvas.update()
    def processUp(self, event):
        self.direction = "up"
    def processDown(self, event):
        self.direction = "down"
    def processLeft(self, event):
        self.direction = "left"
    def processRight(self, event):
        self.direction = "right"
swirl()

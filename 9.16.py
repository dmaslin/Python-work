from tkinter import *

class movingfan:
    def __init__(self):
        window = Tk()
        window.title("Fan")

        self.canvas = Canvas(height = 500, width = 500, bg = "white")
        self.canvas.pack()

        self.start1 = 0
        self.start2 = 90
        self.start3 = 180
        self.start4 = 270
        self.adder = 25
        self.canvas.create_arc(50,50, 450,450, start = self.start1, extent = 45, fill = "red", tags = "arc1") 
        self.canvas.create_arc(50,50, 450,450, start = self.start2, extent = 45, fill = "red", tags = "arc2")
        self.canvas.create_arc(50,50, 450,450, start = self.start3, extent = 45, fill = "red", tags = "arc3")
        self.canvas.create_arc(50,50, 450,450, start = self.start4, extent = 45, fill = "red", tags = "arc4")

        self.animate()
        window.mainloop()
    def animate(self):
        while True:
            self.canvas.delete("arc1", "arc2", "arc3", "arc4")
            self.canvas.create_arc(50,50, 450,450, start = self.start1 + self.adder, extent = 45, fill = "red", tags = "arc1") 
            self.canvas.create_arc(50,50, 450,450, start = self.start2 + self.adder, extent = 45, fill = "red", tags = "arc2")
            self.canvas.create_arc(50,50, 450,450, start = self.start3 + self.adder, extent = 45, fill = "red", tags = "arc3")
            self.canvas.create_arc(50,50, 450,450, start = self.start4 + self.adder, extent = 45, fill = "red", tags = "arc4")
            self.adder += 25
            self.canvas.after(50)
            self.canvas.update()
movingfan()

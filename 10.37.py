from tkinter import *

class interactiveBinarySearch:
    def __init__(self):
        window = Tk()
        window.title("Binary Search Animation")
        frame1 = Frame(window)
        frame1.pack()

        self.canvas = Canvas(window, height = 200, width = 420, bg = "white")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.startup()
        Label(frame, text = "Enter a key (in float): ").pack(side = LEFT)
        self.key = StringVar()
        self.entry = Entry(frame, textvariable = self.key).pack(side = LEFT)
        if self.started == True:
            self.entry.configure(state = DISABLED)
        Button(frame, text = "Step", command = self.binarySearch).pack(side = LEFT)
        Button(frame, text = "Reset", command = self.complete).pack(side = LEFT)
        window.mainloop()
    def startup(self):
        self.started = False
        self.completed = False
        self.num = []
        for i in range(1,21):
            self.num.append(i)
    def binarySearch(self):
        if self.started == False:
            self.low = 1
            self.high = len(self.num) - 1
            self.started = True
        if self.high >= self.low:
            self.mid = (self.low + self.high) // 2
            if int(self.key.get()) < self.num[self.mid]:
                self.high = self.mid - 1
            elif int(self.key.get()) == self.num[self.mid]:
                self.completed = True
            else:
                self.low = self.mid + 1
        else:
            -self.low - 1
        self.nextStep()
        
    def complete(self):
        import tkinter.messagebox
        restart = tkinter.messagebox.askyesno("Restart", "Would you like to Restart?")
        return restart
    def nextStep(self):
        self.canvas.delete("rectangle")
        x = 10
        y = 195
        counter = 0
        for i in range(1,21):
            height = (i/21)*195
            sx = (x+x+20)/2
            if i == self.mid:
                self.canvas.create_rectangle(x, y-height, x + 20, y, fill = "red", tags = "rectangle")
                self.canvas.create_text(sx, y- height - 5, text = str(i))
                x += 20
            elif i >= self.low and i < self.mid:
                self.canvas.create_rectangle(x, y-height, x + 20, y, fill = "grey", tags = "rectangle")
                self.canvas.create_text(sx, y- height - 5, text = str(i))
                x += 20
                counter +=1
            elif self.mid+ counter >= i :
                self.canvas.create_rectangle(x, y-height, x + 20, y, fill = "grey", tags = "rectangle")
                self.canvas.create_text(sx, y- height - 5, text = str(i))
                x += 20
            else:
                self.canvas.create_rectangle(x, y-height, x + 20, y)
                self.canvas.create_text(sx, y- height - 5, text = str(i), tags = "rectangle")
                x += 20
        if self.completed == True:
            yorn =self.complete()
class program:
    binary = interactiveBinarySearch()
    run = True
    while run == True:
        interactiveBinarySearch()
        if binary.complete() == "yes":
            binary.startup()
        else:
            run = False
program()

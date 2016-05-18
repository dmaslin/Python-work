from tkinter import *

class parabola:
    def __init__(self):
        window = Tk()
        window.title("Square Function")
        width = 400
        height = 150
        offset = .01
        frame = Frame(window)
        frame.pack()
        canvas = Canvas(frame, bg = "white", height = height, width = width)
        canvas.pack()
        
        f = []
        for x in range(-350, 350):
            f.append([-1*(x - width/2), -1*((x*x*offset) - height+30)])
        for i in range(len(f) - 1):
            canvas.create_line(f[i],f[i+1])
        canvas.create_line(10, height - 30, width - 20, height - 30, arrow = "last")
        canvas.create_text(width - 10, height - 30, text = "X")
        canvas.create_line(width/2, height - 10, width/2, 20, arrow = "last")
        canvas.create_text(width/2, 10, text = "Y")
        window.mainloop()
parabola()

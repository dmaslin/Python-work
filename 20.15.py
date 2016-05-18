from tkinter import * # Import tkinter
from Graph import Graph
import random
def add(event):
    circles.append([event.x, event.y])
    repaint()

def distance(circle1, circle2):
    return ((circle1[0] - circle2[0]) ** 2 
            + (circle1[1] - circle2[1]) ** 2) ** 0.5
def getColor():
    r = list(hex(random.randint(0,255)))
    g = list(hex(random.randint(0,255)))
    b = list(hex(random.randint(0,255)))

    r.pop(0)
    r.pop(0)
    g.pop(0)
    g.pop(0)
    b.pop(0)
    b.pop(0)
    if len(r) < 2:
        r.insert(0,"0")
    if len(g) < 2:
        g.insert(0,"0")
    if len(b) < 2:
        b.insert(0,"0")
    s = "#"+"".join(r)
    s = s + "".join(g)
    s = s + "".join(b)
    return s


def repaint():
    canvas.delete(ALL)
    if len(circles) == 0: return # Nothing to paint
    elif len(circles) > 1:
        c = []
        cbycolor = []
        for i in range(len(circles)):
            if circles[i] not in cbycolor:
                color = getColor()
                cbycolor.append(circles[i])
                c.append(color)
                for j in range(i+1, len(circles)):
                    if distance(circles[i], circles[j]) <= 2 * radius:
                        c.append(color)
                        cbycolor.append(circles[j])
        counter = 0
        for [x, y] in cbycolor:
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = c[counter], tags = "point")
            counter +=1
    else:
        color = getColor()
        for [x, y] in circles:
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = color, tags = "point")

window = Tk() # Create a window
window.title("ConnectedCircles") # Set title

width = 250
height = 200
radius = 15
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing circles
circles = []

canvas.bind("<Button-1>", add)

window.mainloop() # Create an event loop

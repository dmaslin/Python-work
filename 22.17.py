from tkinter import * # Import tkinter
from Graph import Graph

def add(event):
    squares.append([event.x, event.y])
    repaint()

def repaint():
    canvas.delete(ALL)
    
    if len(squares) == 0: return # Nothing to paint
    tags = 0
    for [x, y] in squares:
        canvas.create_rectangle(x - side, y - side, x + side, y + side, tags = "point")
        tags += 1

    # Build the edges
    edges = []
    isAllSquaresConnected = True
    for i in range(len(squares)):
        x = canvas.find_overlapping(squares[i][0]-side, squares[i][1]-side, squares[i][0]+side , squares[i][1]+side)
        for j in range(i + 1, len(squares)):
            if len(x)  > 1:
                edges.append([i, j])
                edges.append([j, i])
            else:
                isAllSquaresConnected = False

    
    if isAllSquaresConnected:
        canvas.itemconfigure("point", fill = "red")

    
    
            

window = Tk() # Create a window
window.title("ConnectedSquares") # Set title

width = 250
height = 200
side = 15
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing squares
squares = []

canvas.bind("<Button-1>", add)

window.mainloop() # Create an event loop

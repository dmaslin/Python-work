from NineTailModel import NineTailModel
from NineTailModel import getIndex
from NineTailModel import getNode
from NineTailModel import printNode
from tkinter import *

def flipOne(event):
    c = list(coins.get())
    if c[0] == "H":
        c[0] = "T"
        canvas.itemconfig("one", text = c[0])
    else:
        c[0] = "H"
        canvas.itemconfig("one", text = c[0])
    c = "".join(c)
    coins.set(c)
    canvas.update()

    
def flipTwo(event):
    c = list(coins.get())
    if c[1] == "H":
        c[1] = "T"
        canvas.itemconfig("two", text = c[1])
    else:
        c[1] = "H"
        canvas.itemconfig("two", text = c[1])
    c = "".join(c)
    coins.set(c)
    canvas.update()
        
def flipThree(event):
    c = list(coins.get())
    if c[2] == "H":
        c[2] = "T"
        canvas.itemconfig("three", text = c[2])
    else:
        c[2] = "H"
        canvas.itemconfig("three", text = c[2])
    c = "".join(c)
    coins.set(c)
    canvas.update()


def flipFour(event):
    c = list(coins.get())
    if c[3] == "H":
        c[3] = "T"
        canvas.itemconfig("four", text = c[3])
    else:
        c[3] = "H"
        canvas.itemconfig("four", text = c[3])
    c = "".join(c)
    coins.set(c)
    canvas.update()

def flipFive(event):
    c = list(coins.get())
    if c[4] == "H":
        c[4] = "T"
        canvas.itemconfig("five", text = c[4])
    else:
        c[4] = "H"
        canvas.itemconfig("five", text = c[4])
    c = "".join(c)
    coins.set(c)
    canvas.update()

def flipSix(event):
    c = list(coins.get())
    if c[5]  == "H":
        c[5] = "T"
        canvas.itemconfig("six", text = c[5])
    else:
        c[5] = "H"
        canvas.itemconfig("six", text = c[5])
    c = "".join(c)
    coins.set(c)
    canvas.update()

def flipSeven(event):
    c = list(coins.get())
    if c[6] == "H":
        c[6] = "T"
        canvas.itemconfig("seven", text = c[6])
    else:
        c[6] = "H"
        canvas.itemconfig("seven", text = c[6])
    c = "".join(c)
    coins.set(c)
    canvas.update()
    
def flipEight(event):
    c = list(coins.get())
    if c[7] == "H":
        c[7] = "T"
        canvas.itemconfig("eight", text = c[7])
    else:
        c[7] = "H"
        canvas.itemconfig("eight", text = c[7])
    c = "".join(c)
    coins.set(c)
    canvas.update()
        
def flipNine(event):
    c = list(coins.get())
    if c[8] == "H":
        c[8] = "T"
        canvas.itemconfig("nine", text = c[8])
    else:
        c[8] = "H"
        canvas.itemconfig("nine", text = c[8])
    c = "".join(c)
    coins.set(c)
    canvas.update()

def solve():
    c = "".join(coins.get())
    model = NineTailModel()
    path = model.getShortestPath(getIndex(c))
    canvas.delete(ALL)
    x = 10
    y = 10
    canvas.config(width = 50 + (50* len(path)))
    for i in range(len(path)):
        node = getNode(path[i])

        for j in range(3):
            for k in range(3):
                canvas.create_rectangle(x, y, x+10, y + 20)
                canvas.create_text(x + 5, y +  10, text = node[j+k])
                x += 10
            x = x - 30
            y += 20
        x += 50
        y = 10
def clear():
    canvas.delete(ALL)
    coins = "TTTHHHTTT"
    canvas.config(width = 50)
    x = 10
    y = 10
    for i in range(3):
        for k in range(3):
            canvas.create_rectangle(x, y, x+10, y + 20)
            x += 10
        y += 20
        x = 10
    x = 10
    y = 10
    one = canvas.create_text(x + 5, y + 10, text = coins[0], tags = "one")
    two = canvas.create_text(x + 15, y + 10, text = coins[1], tags = "two")
    three = canvas.create_text(x + 25, y + 10, text = coins[2], tags = "three")
    four = canvas.create_text(x + 5, y + 30, text = coins[3], tags = "four")
    five = canvas.create_text(x + 15, y + 30, text = coins[4], tags = "five")
    six = canvas.create_text(x + 25, y + 30, text = coins[5], tags = "six")
    seven = canvas.create_text(x + 5, y + 50, text = coins[6], tags = "seven")
    eight = canvas.create_text(x + 15, y + 50, text = coins[7], tags = "eight")
    nine = canvas.create_text(x + 25, y + 50, text = coins[8], tags = "nine")

    

window = Tk()
window.title("Nine Coins")
canvas = Canvas(window, height = 80, width = 50)
canvas.pack()
    
frame = Frame(window)
frame.pack()
coins = StringVar()
coins.set("TTTHHHTTT")
coin = list(coins.get())
    
Button(frame, text = "Solve", command = solve).pack(side = LEFT)
Button(frame, text = "Clear", command = clear).pack(side = LEFT)

    
x = 10
y = 10
for i in range(3):
    for k in range(3):
        canvas.create_rectangle(x, y, x+10, y + 20)
        x += 10
    y += 20
    x = 10
x = 10
y = 10
one = canvas.create_text(x + 5, y + 10, text = coin[0], tags = "one")
two = canvas.create_text(x + 15, y + 10, text = coin[1], tags = "two")
three = canvas.create_text(x + 25, y + 10, text = coin[2], tags = "three")
four = canvas.create_text(x + 5, y + 30, text = coin[3], tags = "four")
five = canvas.create_text(x + 15, y + 30, text = coin[4], tags = "five")
six = canvas.create_text(x + 25, y + 30, text = coin[5], tags = "six")
seven = canvas.create_text(x + 5, y + 50, text = coin[6], tags = "seven")
eight = canvas.create_text(x + 15, y + 50, text = coin[7], tags = "eight")
nine = canvas.create_text(x + 25, y + 50, text = coin[8], tags = "nine")

canvas.tag_bind(one, "<Button-1>", flipOne)
canvas.tag_bind(two,"<Button-1>", flipTwo)
canvas.tag_bind(three,"<Button-1>", flipThree)
canvas.tag_bind(four,"<Button-1>", flipFour)
canvas.tag_bind(five,"<Button-1>", flipFive)
canvas.tag_bind(six,"<Button-1>", flipSix)
canvas.tag_bind(seven,"<Button-1>", flipSeven)
canvas.tag_bind(eight,"<Button-1>", flipEight)
canvas.tag_bind(nine,"<Button-1>", flipNine)

window.mainloop()




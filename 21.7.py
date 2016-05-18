from tkinter import *
from Map21_7 import Map

def insert():
    if m.getSize() == 0:
        s = int(size.get())
        if s != "" or s != "4":
            m.setInitialCapacity(s)
    k = int(key.get())
    m.put(k, k)
    createMap()

def delete():
    if m.getSize() == 0:
        s = int(size.get())
        if s != "" or s != "4":
            m.setInitialCapacity(s)
    m.remove(int(key.get()))
    createMap()
def removeAll():
    if m.getSize() == 0:
        s = int(size.get())
        if s != "" or s != "4":
            m.setInitialCapacity(s)
    m.clear()
    createMap()

def createMap():
    
    canvas.delete(ALL)
    lst = m.getTable()
    canvas.create_text(200, 10, text = "Table size = "+ str(len(lst))+" Number of keys = "+ str(m.getSize()))
    canvas.create_text(200, 20, text = "Load Factor = "+format((m.getSize() / len(lst)), ".2f") + "Load Factor Threashhold = .75")
    x = 20
    y = 30
    l = 40
    w = 20
    index = []
    for a in range(len(lst)):
        index.append(a)
    for i in range(len(lst)):
        canvas.create_text(10, y + 10, text = str(index[i]))
        canvas.create_rectangle(x, y, x + l, y + w)
        if len(lst[i]) > 0:
            x += 10
            for j in range(0, len(lst[i])):
                canvas.create_line(x, y + 10, x + l, y + 10, fill = "red", arrow = LAST)
                x += l
                canvas.create_rectangle(x, y, x + l, y + w, outline = "red")
                canvas.create_text(x+20, y + 10, text = str(lst[i][j]))
                x += l
            x = 20
        y += w
window = Tk()
window.title("Separate Chaining")
frame = Frame(window)
frame.pack()
xscrollbar = Scrollbar(frame, orient = HORIZONTAL)
xscrollbar.pack(side = BOTTOM)
yscrollbar = Scrollbar(frame)
yscrollbar.pack(side = RIGHT)
canvas = Canvas(frame, height = 200, width = 400, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set, scrollregion = (0,0, 1000, 1000), bg = "white")
canvas.pack(side = LEFT)
xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)
frame1 = Frame(window)
frame1.pack()

Label(frame1, text = "Enter initial table size: ").pack(side = LEFT)
size = StringVar()
size.set("4")
Entry(frame1, width = 2, textvariable = size).pack(side = LEFT)
Label(frame1, text = " Enter a value: ").pack(side = LEFT)
key = StringVar()
Entry(frame1, width = 2, textvariable = key).pack(side = LEFT)
Button(frame1, text = "Insert", command = insert).pack(side = LEFT)
Button(frame1, text = "Delete", command = delete).pack(side = LEFT)
Button(frame1, text = "Remove All", command = removeAll).pack(side = LEFT)
m = Map()
window.mainloop()

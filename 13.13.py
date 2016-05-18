from tkinter import *

f = input("Enter a filename: ")

fin = open(f, "r")
l = fin.readline()
l = list(l)
l = eval(l[0])
v = []
for i in range(l):
    v.append(fin.readline().split(" "))


window = Tk()
window.title("Display a Graph")
canvas = Canvas(window, height = 200, width = 300, bg = "white")
canvas.pack()
for i in range(l):
    canvas.create_oval(eval(v[i][1]) - 2, eval(v[i][2]) -2, eval(v[i][1]) + 2, eval(v[i][2]) +2, fill = "black")
    canvas.create_text(eval(v[i][1]) - 5, eval(v[i][2]) - 5, text = v[i][0])
    for j in range(len(v[i]) - 3):
        if '\n' in v[i][j+3]:
            n = eval(v[i][j+3][0])
        else:
            n = eval(v[i][j+3])
        canvas.create_line(eval(v[i][1]), eval(v[i][2]), eval(v[n][1]), eval(v[n][2]))

window.mainloop()

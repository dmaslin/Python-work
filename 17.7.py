import turtle as t
import random as r
def insertionSort(alist):
    t.speed(0)
    rectW = 20 #width of the rectangles
    rectH = 10 #for each value the rectangle height will be 10 units higher so 3 will be 30, 10 will be 100 and so on
    for i in range(len(alist)):
        t.penup()
        t.goto(-400 + (i*rectW),0)
        t.pendown()
        for j in range(2):
            t.forward(rectW)
            t.left(90)
            t.forward(alist[i]*rectH)
            t.left(90)
    
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            x = alist[position - 1]
            t.color("white")
            t.begin_fill()
            for i in range(position +1):
                t.penup()
                t.goto(-400 + (i*rectW),0)
                t.pendown()
                t.forward(rectW)
                t.left(90)
                t.forward(alist[i]*rectH)
                t.left(90)
                t.forward(rectW)
                t.left(90)
                t.forward(alist[i]*rectH)
                t.left(90)
            t.end_fill()
            alist[position], alist[position - 1]=x, currentvalue
            t.color("black")
            for i in range(position +1):
                t.penup()
                t.goto(-400 + (i*rectW),0)
                t.pendown()
                t.forward(rectW)
                t.left(90)
                t.forward(alist[i]*rectH)
                t.left(90)
                t.forward(rectW)
                t.left(90)
                t.forward(alist[i]*rectH)
                t.left(90)
            position = position-1
        alist[position]=currentvalue
        

x = []

for i in range(1, 21):
    x.append(i)
r.shuffle(x)
insertionSort(x)



print(x)

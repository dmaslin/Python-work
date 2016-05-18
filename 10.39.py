from tkinter import *
from   __future__ import division, print_function
from   itertools  import permutations, combinations, product, \
                         chain
from   pprint     import pprint as pp
from   fractions  import Fraction as F
import random

class twentyfour:

    def __init__(self):       
        window = Tk()
        window.title("Pick Four Cards Randomly")
        self.deck = []
        self.cards = []
        for i in range(1, 53):
            self.deck.append(PhotoImage(file = str(i)+".gif"))
        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text = "Refresh", command = self.shuffle).pack()
        frame = Frame(window)
        frame.pack()
        self.labelList = []
        for i in range(4):
            self.cards.append(i)
            self.labelList.append(Label(frame, image = self.deck[self.cards[i]]))
            self.labelList[i].pack(side = LEFT)
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text ="Enter an Expression: ").pack(side = LEFT)
        self.expression = StringVar()
        Entry(frame2, textvariable = self.expression).pack(side = LEFT)
        Button(frame2, text = "Verify", command = self.verify).pack(side = LEFT)
        window.mainloop()
    def shuffle(self):
        self.cards = []
        for i in range(4):
            x = random.randint(0,51)
            while x in self.cards:
                x = random.randint(0,51)
            self.cards.append(x)
            self.labelList[i]["image"] = self.deck[self.cards[i]]
    def verify(self):
        total = eval(self.expression.get())
        num = 0
        if total == 24:
            for i in range(0,4):
                if str(self.cards[i]%13 + 1) in self.expression.get():
                    num +=1
            if num == 4:
                import tkinter.messagebox
                tkinter.messagebox.showinfo("Correct","You got it!")
            else:
                import tkinter.messagebox
                tkinter.messagebox.showinfo("Incorrect"," You have to use the four cards shown")
        else:
            import tkinter.messagebox
            tkinter.messagebox.showinfo("Incorrect",self.expression.get()+" does not equal 24")
twentyfour()

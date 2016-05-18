from tkinter import *
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
        Button(frame1, text = "Solve", command = self.solve).pack(side = LEFT)
        self.solution = StringVar()
        Entry(frame1, textvariable = self.solution).pack(side = LEFT)
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
    def solve(self):
        a = str(self.cards[0]%13 + 1)
        b = str(self.cards[1]%13 + 1)
        c = str(self.cards[2]%13 + 1)
        d = str(self.cards[3]%13 + 1)
        allCombinations =  [[a, b, c, d], [d, a, b, c],[c, d, a, b], [b, c, d, a],
                         [a, b, d, c], [c, a, b, d],[d, c, a, b], [b, d, c, a],
                         [a, d, c, b], [b, a, d, c],[c, b, a, d], [d, c, b, a],
                         [a, c, b, d], [d, a, c, b],[b, d, a, c], [c, b, d, a],
                         [b, a, c, d], [d, b, a, c],[c, d, b, a], [a, c, d, b],
                         [a, d, b, c], [c, a, d, b],[b, c, a, d], [d, b, c, a]]
        operators = ["+", "-", "*", "/"]
        for i0 in range(len(operators)):
            firstOp = operators[i0]
            for i1 in range(len(operators)):
                secondOp = operators[i1]
                for i2 in range(len(operators)):
                    thirdOp = operators[i2]
                    for i3 in range(len(allCombinations)):
                        cardNums = allCombinations[i3]
                        for i in range(3):
                            for j in range(5):
                                if (i == 0):
                                    if (j == 0):
                                        sol = cardNums[0] + firstOp+ cardNums[1] + secondOp+ cardNums[2] + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 1):
                                        sol = "(" + cardNums[0] + firstOp+ cardNums[1] + ")" + secondOp+ cardNums[2] + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 2):
                                        sol = cardNums[0] + firstOp + "("+ cardNums[1] + secondOp+ cardNums[2] + ")" + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 3):
                                        sol = cardNums[0] + firstOp+ cardNums[1] + secondOp + "("+ cardNums[2] + thirdOp+ cardNums[3] + ")"
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 4):
                                        sol = "(" + cardNums[0] + firstOp+ cardNums[1] + ")" + secondOp+ "(" + cardNums[2] + thirdOp+ cardNums[3] + ")"
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                elif (i == 1):
                                    if (j == 0):
                                        sol = "(" + cardNums[0] + firstOp+ cardNums[1] + secondOp+ cardNums[2] + ")" + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 1):
                                        sol = "((" + cardNums[0] + firstOp+ cardNums[1] + ")" + secondOp+ cardNums[2] + ")" + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 2):
                                        sol = "(" + cardNums[0] + firstOp+ "(" + cardNums[1] + secondOp+ cardNums[2] + "))" + thirdOp+ cardNums[3]
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                elif (i == 2):
                                    if (j == 0):
                                        sol = cardNums[0] + firstOp + "("+ cardNums[1] + secondOp+ cardNums[2] + thirdOp+ cardNums[3] + ")"
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 1):
                                        sol = cardNums[0] + firstOp + "(("+ cardNums[1] + secondOp+ cardNums[2] + ")" + thirdOp+ cardNums[3] + ")"
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
                                    elif (j == 2):
                                        sol = cardNums[0] + firstOp + "("+ cardNums[1] + secondOp + "("+ cardNums[2] + thirdOp+ cardNums[3] + "))"
                                        if (eval(sol) == 24):
                                            self.solution.set(sol)
                                            return
        self.solution.set("No Solution")
twentyfour()

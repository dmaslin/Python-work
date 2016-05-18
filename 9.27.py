from tkinter import *

class interest:
    def __init__(self):
        window = Tk()
        window.title("Compare Interest Rates")

        frame = Frame(window)
        frame.pack()
        Label(frame, text = "Loan Amount").pack(side = LEFT)
        self.loan = StringVar()
        Entry(frame, textvariable = self.loan, justify = RIGHT).pack(side = LEFT)
        Label(frame, text = "Years").pack(side = LEFT)
        self.years = StringVar()
        Entry(frame, textvariable = self.years, justify = RIGHT).pack(side = LEFT)

        Button(frame, text = "Calculate", command = self.calculate).pack(side = LEFT)

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)

        self.text = Text(frame1, width = 68, height = 20, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)

        self.text.insert(END, "Interest Rate" + "\t\t\t" + "Monthly Payment \t\t\tTotalPayment")

        window.mainloop()

    def calculate(self):
        loan = float(self.loan.get())
        years = int(self.years.get())
        interest = 5
        for i in range(0, 25):
            monthly = (loan * (interest/1200)) / (1 - 1 /(1 + (interest/1200))** (years * 12))
            total = monthly * 12 * years
            self.text.insert(END,"\n"+format(interest, ".2f")+"\t\t    "+format(monthly, "10.2f")+"\t\t\t      "+format(total, "10.2f"))
            interest +=.125
interest()

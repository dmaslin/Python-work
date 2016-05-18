from tkinter import *
import tkinter.messagebox

class BirthdayGUI:
    def __init__(self):
        window = Tk()
        window.title("Guess Birthday")
        frame = Frame(window)
        frame.grid(columnspan = 6, sticky = N)
        frame2 = Frame(window, relief = SUNKEN, borderwidth = 1)
        frame2.grid(row = 2, column = 1)
        frame3 = Frame(window, relief = SUNKEN, borderwidth = 1)
        frame3.grid(row = 2, column = 2)
        frame4 = Frame(window, relief = SUNKEN, borderwidth = 1)
        frame4.grid(row = 2, column = 3)
        frame5 = Frame(window, relief = SUNKEN, borderwidth = 1)
        frame5.grid(row = 2, column = 4)
        frame6 = Frame(window, relief = SUNKEN, borderwidth = 1)
        frame6.grid(row = 2, column = 5)
        frame7 = Frame(window)
        frame7.grid(columnspan = 6, sticky = S)
        Label(frame2, text =  "1  3  5  7\n\n9 11 13 15\n\n17 19 21 23\n\n25 27 29 31").pack()
        Label(frame3, text =  "2  3  6  7\n\n10 11 14 15\n\n18 19 22 23\n\n26 27 30 31").pack()
        Label(frame4, text =  "4  5  6  7\n\n12 13 14 15\n\n20 21 22 23\n\n28 29 30 31").pack()
        Label(frame5, text =  "8  9  10 11\n\n12 13 14 15\n\n24 25 26 27\n\n28 29 30 31").pack()
        Label(frame6, text =  "16 17 18 19\n\n20 21 22 23\n\n24 25 26 27\n\n28 29 30 31").pack()
        Label(frame, text = "Check the boxes if your birthday is in these sets").pack()

        self.bday1 = IntVar()
        cbtBirthday1 = Checkbutton(frame2, variable = self.bday1).pack()
        self.bday2 = IntVar()
        cbtBirthday2 = Checkbutton(frame3, variable = self.bday2, onvalue = 2).pack()
        self.bday3 = IntVar()
        cbtBirthday3 = Checkbutton(frame4, variable = self.bday3, onvalue = 4).pack()
        self.bday4 = IntVar()
        cbtBirthday4 = Checkbutton(frame5, variable = self.bday4, onvalue = 8).pack()
        self.bday5 = IntVar()
        cbtBirthday5 = Checkbutton(frame6, variable = self.bday5, onvalue = 16).pack()

        Button(frame7, text = "Guess Birthday", command = self.findBirthday, borderwidth = 2).pack()

        window.mainloop()

    def findBirthday(self):
        day = self.bday1.get() + self.bday2.get() + self.bday3.get() + self.bday4.get() + self.bday5.get()

        tkinter.messagebox.showinfo("Found it", "Your birthday is "+str(day))
BirthdayGUI()

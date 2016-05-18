import random
from tkinter import *


class Hangman:
    def __init__(self):
        f = open("hangman.txt", "r")
        words = f.read().split()
        rword = random.randint(0, len(words) - 1)
        self.hword = words[rword]
        self.hword = list(self.hword)
        f.close()
        self.misses = 0
        self.display = []
        for i in range(len(self.hword)):
            self.display.append("*")
        window = Tk()
        window.title("Hangman Game")

        self.canvas = Canvas(window, height = 300, width = 400, bg = "white")
        self.canvas.pack()
        self.canvas.create_line(5,290, 35, 290)
        self.canvas.create_line(20, 290, 20, 10)
        self.canvas.create_line(20, 10, 100, 10)
        self.canvas.bind("<Key>", self.hangman)
        self.canvas.focus_set()
        stars = ""
        self.missedLetters = ""
        for i in range(len(self.hword)):
            stars += self.display[i]
        self.canvas.create_text(100, 225, text = "The word is : "+ stars, tags = "string")
        window.mainloop()
    def hangman(self, event):
        word = self.hword
        letterIndex = []
        if event.char in word and event.char not in self.display:
            numInWord = word.count(event.char)
            for a in range(0, len(word)):
                if word[a] == event.char:
                    letterIndex.append(a)
            for b in range(0,numInWord):
                self.display[letterIndex[b]] = event.char
            stars = ""
            for a in range(len(self.display)):
                stars += self.display[a]
            self.canvas.delete("string")
            self.canvas.create_text(100, 225, text = "The word is : "+ stars, tags = "string")
            if self.display == word:
                self.canvas.delete("wrong")
                self.canvas.unbind("<Key>")
                self.canvas.create_text(100, 250, text = "To continue the game press ENTER")
                self.canvas.bind("<Return>", self.complete)
                self.canvas.focus_set()
        else:
            self.canvas.delete("wrong")
            self.missedLetters += event.char
            self.canvas.create_text(100, 250, text = "Missed Letters : "+ self.missedLetters, tags = "wrong")
            self.misses += 1
            self.mistake()
            if self.misses == 7:
                self.canvas.delete("string", "wrong")
                word = "".join(word)
                self.canvas.create_text(100, 225, text = "The word is : "+ word)
                self.canvas.create_text(100, 250, text = "To continue the game press ENTER")
                self.canvas.bind("<Return>", self.complete())
                self.canvas.focus_set()
    def complete(self, event):
        self.misses = 0
        f = open("hangman.txt", "r")
        words = f.read().split()
        rword = random.randint(0, len(words) - 1)
        self.hword = words[rword]
        self.hword = list(self.hword)
        f.close()
        self.misses = 0
        self.display = []
        for i in range(len(self.hword)):
            self.display.append("*")
        self.canvas.delete(ALL)
        self.canvas.unbind("<Return>")
        self.canvas.bind("<Key>", self.hangman)
        self.canvas.focus_set()
        self.canvas.create_line(5,290, 35, 290)
        self.canvas.create_line(20, 290, 20, 10)
        self.canvas.create_line(20, 10, 100, 10)
        self.canvas.bind("<Key>", self.hangman)
        self.canvas.focus_set()
        stars = ""
        self.missedLetters = ""
        for i in range(len(self.hword)):
            stars += self.display[i]
        self.canvas.create_text(100, 225, text = "The word is : "+ stars, tags = "string")
    def mistake(self):
        strike = self.misses
        if strike == 1:
            self.canvas.create_line(100, 10, 100,20)
        elif strike == 2:
            self.canvas.create_oval(75, 20, 125, 70)
        elif strike == 3:
            self.canvas.create_line(75, 70, 50, 90)
        elif strike == 4:
            self.canvas.create_line(125, 70, 150, 90)
        elif strike == 5:
            self.canvas.create_line(100, 70, 100, 200)
        elif strike == 6:
            self.canvas.create_line(75, 200, 50, 220)
        elif strike == 7:
            self.canvas.create_line(125, 200, 150, 220)
Hangman()

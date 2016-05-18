from tkinter import *

class Sudoku:

    def __init__(self):

        window = Tk()
        window.title("Sudoku")
        frame = Frame(window)
        frame.pack()

        self.values = []
        self.value = []
        for i in range(9):
            self.values.append([])
            self.value.append([])
            for j in range(9):
                self.value[i].append(StringVar())
                self.value[i][j].set("")
                self.values[i].append(IntVar())
        self.e = []
        for i in range(9):
            self.e.append([])
            for j in range(9):
                self.e[i].append(Entry(frame, width = 2, justify = RIGHT, textvariable = self.value[i][j]))
                self.e[i][j].grid(row = i, column = j)

        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text = "Solve", command = self.isValidGrid).pack(side = LEFT)
        Button(frame1, text = "Clear", command = self.clear).pack(side = LEFT)
        window.mainloop()            

    #Cear the contents of the cells
    def clear(self):
        for i in range(9):
            for j in range(9):
                self.e[i][j].delete(0, END)
                self.e[i][j].configure(bg = "white")
                self.values[i][j].set(StringVar())
                self.values[i][j].set("")
    # Obtain a list of free cells from the puzzle
    def getFreeCellList(self):
        self.freeCellList = []
        for i in range(9):
            for j in range(9):
                if self.value[i][j].get() ==  "":
                    self.freeCellList.append([i, j])
                    self.values[i][j].set(0)
                else:
                    self.e[i][j].configure(bg = "grey")

    # Display the values in the grid 
    def printGrid(self):
        for i in range(9):
            for j in range(9):
                self.value[i][j].set(str(self.values[i][j].get()))
                
    # Search for a solution 
    def search(self):
        self.getFreeCellList()
        numberOfFreeCells = len(self.freeCellList)
        if numberOfFreeCells == 0:
            return # No free cells
        
        k = 0 # Start from the first free cell
        while True:
            i = self.freeCellList[k][0]
            j = self.freeCellList[k][1]
            if self.values[i][j].get() == 0:
              self.values[i][j].set(1) # Fill the free cell with number 1
        
            if self.isValid(i, j):
              if k + 1 == numberOfFreeCells:
                  self.printGrid()# A solution is found
                  return
              else:
                # Move to the next free cell
                print("moved")
                k += 1
            elif self.values[i][j].get() < 9:
              # Fill the free cell with the next possible value
              self.values[i][j].set(self.values[i][j].get() + 1 )
            else:
              # grid[i][j] is 9, backtrack
              while self.values[i][j].get() == 9:
                if k == 0:
                  import tkinter.messagebox # No possible value
                  tkinter.messagebox.showerror("Error", "There is no solution")
                  self.clear()
                self.values[i][j].set(0) # Reset to free cell
                k -= 1 # Backtrack to the preceding free cell
                i = self.freeCellList[k][0]
                j = self.freeCellList[k][1]
        
              # Fill the free cell with the next possible value, 
              # search continues from this free cell at k
              self.values[i][j].set(self.values[i][j].get() + 1) 
        
        self.printGrid() # A solution is found

    # Check whether grid[i][j] is valid in the grid 
    def isValid(self, i, j):
        # Check whether grid[i][j] is valid at the i's row
        for column in range(9):
            if column != j and self.values[i][column].get() == self.values[i][j].get():
              return False
        
        # Check whether grid[i][j] is valid at the j's column
        for row in range(9):
            if row != i and self.values[row][j].get() == self.values[i][j].get():
              return False
        
        return True # The current value at grid[i][j] is valid

    # Check whether the fixed cells are valid in the grid 
    def isValidGrid(self):
        for r in range(9):
            for c in range(9):
                if self.value[r][c].get() == "":
                    self.values[r][c].set(0)
                else:
                    self.values[r][c].set(int(self.value[r][c].get()))
        for i in range(9):
            for j in range(9):
                if self.values[i][j].get() < 0 or self.values[i][j].get() > 9 or (self.values[i][j].get() != 0 and not self.isValid(i, j)): 
                    import tkinter.messagebox
                    tkinter.messagebox.showerror("Error", "Invalid input, please try again")
                    self.clear()

        self.search() # The fixed cells are valid

Sudoku()

from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def showResult():
    analyzeFile(filename.get())

def analyzeFile(filename):
    try:
        infile = open(filename, "r") # Open the file
    
        counts = 26 * [0] # Create and initialize counts
        for line in infile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)
        
        # Display results
        x = 5
        for i in range(len(counts)):
            y = 200-(195 * (counts[i]/max(counts)))
            canvas.create_rectangle(x, y, x+20, 200)
            canvas.create_text(x + 10, 210, text = chr(97 + i))
            x += 20
        infile.close() # Close file
    except IOError:
        tkinter.messagebox.showwarning("Analyze File", 
                                    "File " + filename + " does not exist")  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
            
def openFile(): 
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)
        
window = Tk() # Create a window
window.title("Occurrence of Letters") # Set title

frame1 = Frame(window) # Hold four labels for displaying cards
frame1.pack()

canvas = Canvas(frame1, height = 220, width = 530, bg = "white")
canvas.pack()
canvas.create_line(5, 200, 525, 200)

frame2 = Frame(window) # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 20, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = openFile).pack(side = LEFT)
Button(frame2, text = "Show Result", command = showResult).pack(side = LEFT)

window.mainloop() # Create an event loop

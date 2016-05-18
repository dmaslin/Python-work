from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
import urllib.request

def showResult():
    analyzeFile(url.get())

def analyzeFile(url):
    try:
        infile = urllib.request.urlopen(url)
        s = str(infile.read().decode()) # Read the content as string from the URL
    
        counts = countLetters(s.lower())

        # Display results
        x = 5
        print(counts)
        for i in range(len(counts)):
            y = 200-(195 * (counts[i]/max(counts)))
            canvas.create_rectangle(x, y, x+20, 200)
            canvas.create_text(x + 10, 210, text = chr(97 + i))
            x += 20
        infile.close() # Close file
    except ValueError:
        tkinter.messagebox.showwarning("Analyze URL", 
                                    "URL " + filename + " does not exist")  

# Count each letter in the string 
def countLetters(s): 
    counts = 26 * [0] # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts

            
def openFile(): 
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)
        
window = Tk() # Create a window
window.title("Occurrence of Letters from URL") # Set title

frame1 = Frame(window) # Hold four labels for displaying cards
frame1.pack()


canvas = Canvas(frame1, height = 220, width = 530, bg = "white")
canvas.pack()
canvas.create_line(5, 200, 525, 200)

frame2 = Frame(window) # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text = "Enter a URL: ").pack(side = LEFT)
url = StringVar()
Entry(frame2, width = 50, textvariable = url).pack(side = LEFT)
Button(frame2, text = "Show Result", command = showResult).pack(side = LEFT)

window.mainloop() # Create an event loop

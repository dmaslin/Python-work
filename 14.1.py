import os.path
import sys

def main():
    keyWords = {"and", "as", "assert", "break", "class", 
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):  # Check if target file exists
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r") # Open files for input 
    
    text = infile.read().split() # Read and split words from the file 
    words = []
    count = 0
    for word in text:
        if word in keyWords:
            count += 1
            words.append(word)
    words = set(words)#convert to set to remove repeats 
    words = list(words)#convert back to list to make itterable
    
    
    print("The number of keywords in", filename, "is", count)
    print("The keywords are ", end = "")
    for i in range(len(words)):
        print(words[i], end = ", ")
    
    
main()

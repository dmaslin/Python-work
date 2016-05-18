import random
def hangman(word):
    display = []
    print("(Guess) Enter a letter in word ", end = "")
    for i in range(0, len(word)):
        print("*", end = "")
        display.append("*")
    guess = input(" > ")
    misses = 0
    numInWord = 0
    letterIndex = []
    while display != word:
        if guess in word and guess not in display:
            numInWord = word.count(guess)
            for a in range(0, len(word)):
                if word[a] == guess:
                    letterIndex.append(a)
            for b in range(0,numInWord):
                display[letterIndex[b]] = guess
            letterIndex = []
            if display == word:
                return misses
        elif guess in display:
            print(guess + " has already been used.")
        else:
            misses += 1
            print(guess +" is not in the word.")
        print("(Guess) Enter a letter in word ", end = "")
        for i in range(0, len(display)):
            print(display[i], end = "")
        guess = input(" > ")
play = "y"

while play == "y":
    f = open("hangman.txt", "r")
    words = f.read().split()
    rword = random.randint(0, len(words) - 1)
    hword = words[rword]
    hword = list(hword)
    f.close()

    mistakes = hangman(hword)
    if mistakes == 1:
        print("The word is "+words[rword]+". You missed "+str(mistakes)+" time.")
    elif mistakes > 1:
        print("The word is "+words[rword]+". You missed "+str(mistakes)+" times.")
    elif mistakes == 0:
        print("The word is "+words[rword]+". You didn't miss any.")
    print("")
    play = input("Do you want to guess another word? Enter y or n> ")

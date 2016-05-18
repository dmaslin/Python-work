def counts(char):
    counter = 0
    for i in range(1, len(char)+1):
        tf = countsHelper(char, i)
        if tf == True:
            counter +=1
    print("There are "+str(counter)+" capital characters in the list")
    


def countsHelper(char, high):
    if ord(char[len(char) - high]) >= 65 and ord(char[len(char) - high]) <= 90:
        return True
    else:
        return False

lst = input("Enter a list of characters separated by comma and space: ")

lst = lst.split(", ")

counts(lst)

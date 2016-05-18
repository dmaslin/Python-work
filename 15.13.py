def countUppercase(s):
    count = 0
    for i in range(1, len(s) + 1):
        tf = countUppercaseHelper(s, i)
        if tf == True:
            count += 1
    print("There are "+str(count)+" capital letters in the string")
def countUppercaseHelper(s, high):
    if ord(s[len(s) - high]) >= 65 and ord(s[len(s) - high]) <= 90:
        return True
    else:
        return False

s = input("Enter a string: ")

countUppercase(s)

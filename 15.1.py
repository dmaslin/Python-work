def sumDigits(n):
    num = str(n)
    num = list(num)
    num[1] = str(int(num[0]) + int(num[1]))
    num.pop(0)
    num = "".join(num)
    if len(num) > 1:
        sumDigits(int(num))
    else:
        print(int(num))

def printDigits(n):

    n = list(str(n))

    for i in range(len(n)):
        if i != len(n) - 1:
            print(str(n[i])+" + ", end = "")
        else:
            print(str(n[i])+" = ", end = "")
    n = "".join(n)
    n = int(n)
    sumDigits(n)
    


n = eval(input("Enter a number: "))
printDigits(n)



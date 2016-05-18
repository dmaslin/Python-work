def update(ttt):
    for row in range(3):
        print("-------------")
        print("|", end = "")
        for column in range(3):
            print(ttt[row][column],end = "")
        print("")
    print("-------------")
def check(s):
    if s[0][0] == True and s[1][1] == True and s[2][2] == True:
        return True
    elif s[0][2] == True and s[1][1] == True and s[2][0] == True:
        return True
    elif s[0][0] == True and s[0][1] == True and s[0][2] == True:
        return True
    elif s[1][0] == True and s[1][1] == True and s[1][2] == True:
        return True
    elif s[2][0] == True and s[2][1] == True and s[2][2] == True:
        return True
    elif s[0][0] == True and s[1][0] == True and s[2][0] == True:
        return True
    elif s[0][1] == True and s[1][1] == True and s[2][1] == True:
        return True
    elif s[0][2] == True and s[1][2] == True and s[2][2] == True:
        return True
    else:
        return False
ttt = []
for row in range(3):
    ttt.append([])
    for column in range(3):
        ttt[row].append("   |")
for row in range(3):
    print("-------------")
    print("|", end = "")
    for column in range(3):
        print(ttt[row][column],end = "")
    print("")
print("-------------")

x = []
o = []

for row in range(3):
    x.append([])
    o.append([])
    for column in range(3):
        x[row].append(False)
        o[row].append(False)

victoryO = False
victoryX = False
numtaken = 0
while numtaken < 9:
    xr = eval(input("Enter a row (0, 1, or 2) for player X: "))
    xc = eval(input("Enter a column (0, 1, or 2) for player X: "))
    if o[xr][xc] == False:
        x[xr][xc] = True
        ttt[xr][xc] = " X |"
    else:
        while o[xr][xc] == True:
            print("Sorry that position has been taken")
            xr = eval(input("Enter a row (0, 1, or 2) for player X: "))
            xc = eval(input("Enter a column (0, 1, or 2) for player X: "))
        x[xr][xc] = True
        ttt[xr][xc] = " X |"
    update(ttt)
    victoryX = check(x)
    numtaken +=1
    if numtaken == 9:
        break
    if victoryX == True:
        break
    orow = eval(input("Enter a row (0, 1, or 2) for player O: "))
    oc = eval(input("Enter a column (0, 1, or 2) for player O: "))
    if x[orow][oc] == False:
        o[orow][oc] = True
        ttt[orow][oc] = " O |"
    else:
        while x[orow][oc] == True:
            print("Sorry that position has been taken")
            orow = eval(input("Enter a row (0, 1, or 2) for player O: "))
            oc = eval(input("Enter a column (0, 1, or 2) for player O: "))
        o[orow][oc] = True
        ttt[orow][oc] = " O |"
    update(ttt)
    victoryO= check(o)
    numtaken 
    if victoryO == True:
        break
if victoryX == True:
    print("X player won")
elif victoryO == True:
    print("O player won")
elif numtaken == 9:
    print("Its a Tie")

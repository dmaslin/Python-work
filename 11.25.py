def isMarkovMatrix(m):
    pos = True
    equals1 = True
    if len(m) == len(m[0]):
        for c in range(len(m)):
            total = 0
            for r in range(len(m)):
                if m[r][c] > 0:
                    total += m[r][c]
                else:
                    pos = False
            if total != 1:
                equals1 = False
    else:
        return False
    if pos == False or equals1 == False:
        return False
    elif pos == True and equals1 == True:
        return True
print("Enter a 3-by-3 matrix row by row:")

m = []
for r in range(3):
    m.append([])
    s = input()
    s = s.split(" ")
    for c in range(3):
        m[r].append(eval(s[c]))
mm = isMarkovMatrix(m)

if mm == True:
    print("It is a Markov Matrix")
else:
    print("It is not a Markov Matrix")

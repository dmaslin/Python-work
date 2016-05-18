def solveQuadratic(equ, roots):
    r = []
    if roots > 0:
        r.append((-(equ[1])-((equ[1])**2 - 4*equ[0]*equ[2])**.5) /(2*equ[0]))
        r.append((-(equ[1])+((equ[1])**2 - 4*equ[0]*equ[2])**.5) /(2*equ[0]))
        return r
    elif roots == 0:
        r.append((-(equ[1])-((equ[1])**2 - 4*equ[0]*equ[2])**.5) /(2*equ[0]))
        return r
equ = input("Enter a, b, and c separated by a space: ")
equ = equ.split()
for i in range(0,3):
    equ[i] = int(equ[i])
if ((equ[1])**2 - 4*equ[0]*equ[2])**.5 > 0:
    roots = 2
    answers = solveQuadratic(equ, roots)
    print("The number of roots are "+ str(roots))
    print("Their values are ", end = "")
    print(str(answers[0])+" and "+str(answers[1]))
        
elif ((equ[1])**2 - 4*equ[0]*equ[2])**.5 == 0:
    roots = 1
    answers = solveQuadratic(equ, roots)
    print("The number of roots is "+ str(roots))
    print("The value is "+str(answers[0]))
else:
    roots = 0
    print("There are no roots")
    print("There are no values")



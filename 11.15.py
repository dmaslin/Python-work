def sameLine(points):
    x0 = points[0][0]
    y0 = points[0][1]
    x1 = points[1][0]
    y1 = points[1][1]

    numInLine = 2
    for r in range(2, len(points)):
        x2 = points[r][0]
        y2 = points[r][1]
        if (x1 -x0)*(y2 - y0) - (x2 - x0)*(y1-y0) == 0:
            numInLine += 1
    if numInLine == len(points):
        return True
    else:
        return False

s = input("Enter five points: ")

s = s.split(" ")

p = []
for r in range(5):
    p.append([])
    for c in range(2):
        p[r].append(eval(s[(r*2)+c]))
if sameLine(p) == True:
    print("The five points are on the same line")
else:
    print("The five points are not on the same line")

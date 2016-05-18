def getIntersectingPoint(points):
    a = points[0][1] - points[1][1]
    b = points[0][0] - points[1][0]
    c = a * points[0][0] - b * points[0][1]
    d = points[2][1] - points[3][1]
    e = points[2][0] - points[3][0]
    f = d * points[2][0] - d * points[2][1]
    div = a*e - b*d
    if div == 0:
        return False, False
    else:
        x = (c*e - b*f)/div
        y = (a*f - c*e)/div
        return x, y

points = [[],[],[],[]]
for r in range(2):
    s = input("Enter the points of the first line: ").split()
    for f in range(2):
        for c in range(2):
            points[f + (r*2)].append(eval(s[c + (2*f)]))
x, y = getIntersectingPoint(points)

if x == False:
    print("The lines are parallel")
else:
    print("The intersecting points are "+format(x, ".4f")+", "+format(y, ".4f"))

def getTriangleArea(points, p):
    x1, y1, x2, y2= points[0], points[1], points[2], points[3],
    x3, y3 = getIntersectingPoint(p)

    # Compute the length of the three sides
    side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
    side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

    s = (side1 + side2 + side3) / 2;
    temp = s * (s - side1) * (s - side2) * (s - side3)
    area = temp ** 0.5

    if temp < 0 or temp <= 0.0000000000001: return None
    else: return area

def getIntersectingPoint(points):
    a = points[0][1] - points[2][1]
    b = points[0][0] - points[2][0]
    c = a * points[2][0] - b * points[2][1]
    d = points[1][1] - points[3][1]
    e = points[1][0] - points[3][0]
    f = d * points[1][0] - d * points[1][1]
    div = a*e - b*d
    if div == 0:
        return False, False
    else:
        x = (c*e - b*f)/div
        y = (a*f - c*e)/div
        return x, y
p = []
s = input("Enter the four points of each corner: ").split()
for r in range(4):
    p.append([])
    for c in range(2):
        p[r].append(eval(s[c + (2*r)]))
area = []
points = [p[0][0], p[0][1], p[1][0], p[1][1]]
area.append(getTriangleArea(points, p))
points = [p[1][0], p[1][1], p[2][0], p[2][1]]
area.append(getTriangleArea(points, p))
points = [p[2][0], p[2][1], p[3][0], p[3][1]]
area.append(getTriangleArea(points, p))
points = [p[3][0], p[3][1], p[0][0], p[0][1]]
area.append(getTriangleArea(points, p))
area = sorted(area)
print("The areas are ",end = "")
for x in range(len(area)):
    print(format(area[x], ".2f"),end = " ")

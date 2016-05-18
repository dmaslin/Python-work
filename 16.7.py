def distance(p1, p2):
    d = ((p1[0] - p2[0])**2 + (p1[1] -p2[1])**2 )**.5
    return d
def sortY(p):
    y = []
    for i in range(len(p)):
        y.append([])
        y[i].append(p[i][1])
        y[i].append(p[i][0])
    y.sort()
    for i in range(len(p)):
        p[i][0] = y[i][1]
        p[i][1] = y[i][0]
    return p
def lrStrips(p, p1, p2, midx, midy, d):
    lStrip = []
    
    rStrip = []

    for i in range(len(p)):
        if p[i] in p1 and midx - p[i][0] <= d:
            lStrip.append(p[i])
        elif p[i] in p2 and p[i][0] - midx <= d:
            rStrip.append(p[i])
    return lStrip, rStrip
def step3(p, p1, p2, midx, midy, d):
    stripL, stripR = lrStrips(p, p1, p2, midx, midy, d)
    r = 0
    p1i = 0
    p2i = 0
    for x in range(len(stripL)):
        while r < len(stripR) and stripR[r][1] <= stripL[x][1] - d:
            r += 1
        r1 = r
        while (r1 < len(stripR) and ((stripR[r1][1] - stripL[x][1])**2 )**.5 <= d):
            if distance(stripL[x], stripR[r1]) < d:
                d = distance(stripL[x], stripR[r1])
                p1i = x
                p2i = r1
            r1 += 1
    print("The closest two points are "+str(stripL[p1i][0])+", "+str(stripL[p1i][1])+" and "+str(stripR[p2i][0])+", "+str(stripR[p2i][1]))
points = input("Enter the series of points: ").split()
p = []
for i in range(len(points)//2):
    p.append([])
    p[i].append(eval(points[0 + (i+2)]))
    p[i].append(eval(points[1 + (i+2)]))

p.sort()

p1 = []

p2 = []

for i in range((len(p) // 2) +1):
    p1.append(p[i])
for j in range(len(p1), len(p)):
    p2.append(p[j])
midx = p1[len(p1)-1][0]
midy = p1[len(p1)-1][1]
d1 = []
d2 = []


for i in range(len(p2) -1):
    d1.append(distance(p2[i], p2[i+1]))
for i in range(len(p1) - 1):
    d2.append(distance(p1[i], p1[i+1]))
d = min(d1, d2)
d = min(d)
p = sortY(p)
step3(p, p1, p2, midx, midy, d)







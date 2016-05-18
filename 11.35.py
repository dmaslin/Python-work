def distance(points):
    x1, x2, y1, y2 = points[0][0], points[1][0], points[0][1], points[1][1]

    d = ((x2 - x1)**2 + (y2 - y1)**2 )**.5
    return d 
city = []

n = eval(input("Enter the number of cities: "))

if n%2 == 1:
    s = input("Enter the coordinates of the cities: ").split()
    for r in range(n):
        city.append([])
        for c in range(2):
            city[r].append(eval(s[c + (r*2)]))
    d = 0
    for town in range(n):
        for r in range(n):
            points = [[city[town][0], city[town][1]],[city[r][0], city[r][1]]]
            dis = distance(points)
            if dis > d:
                d = dis
                p1 = town
                p2 = r
            #find the largest distance and then will omit them in the next check
    left = []
    for r in range(n-2):
        left.append([])
    count = 0
    p = [p1, p2]
    for r in range(0, n):
        if r not in p:
            left[count].append(city[r][0])
            left[count].append(city[r][1])
            count +=1
    eliminated = 2
    counter = 0
    eliminated = 2
    while len(left) != 1:
        d = 100
        for r in range(n):
            if r not in p:
                points = [[city[p[counter]][0], city[p[counter]][1]],[city[r][0], city[r][1]]]
                dis = distance(points)
                if dis < d:
                    d = dis
                    p1 = town
                    p2 = r
        p.append(p2)
        counter +=1
        eliminated += 1
        d = 100
        for r in range(n):
            if r not in p:
                points = [[city[p[counter]][0], city[p[counter]][1]],[city[r][0], city[r][1]]]
                dis = distance(points)
                if dis < d:
                    d = dis
                    p2 = r
        p.append(p2)
        counter +=1
        eliminated += 1
        c = (len(city)) - eliminated
        left = []
        for i in range(c):
            left.append([])
        c = 0
        for r in range(n):
            if r not in p:
                left[c].append(city[r][0])
                left[c].append(city[r][1])
                c +=1

    print("The central most city is at "+str(left[0][0])+", "+str(left[0][1]))

else: #
    s = input("Enter the coordinates of the cities: ").split()
    for r in range(n):
        city.append([])
        for c in range(2):
            city[r].append(eval(s[c + (r*2)]))
    d = 0
    
    for town in range(n):
        for r in range(n):
            points = [[city[town][0], city[town][1]],[city[r][0], city[r][1]]]
            dis = distance(points)
            if dis > d:
                d = dis
                p1 = town
                p2 = r
            #find the largest distance and then will omit them in the next check
    left = []
    for r in range(n-2):
        left.append([])
    count = 0
    p = [p1, p2]
    for r in range(n):
        if r not in p:
            left[count].append(city[r][0])
            left[count].append(city[r][1])
            count +=1
    counter = 0
    eliminated = 2
    while len(left) != 2:
        d = 100
        for r in range(n):
            if r not in p:
                points = [[city[p[counter]][0], city[p[counter]][1]],[city[r][0], city[r][1]]]
                dis = distance(points)
                if dis < d:
                    d = dis
                    p1 = town
                    p2 = r
        p.append(p2)
        counter +=1
        eliminated +=1
        d = 100
        for r in range(n):
            if r not in p:
                points = [[city[p[counter]][0], city[p[counter]][1]],[city[r][0], city[r][1]]]
                dis = distance(points)
                if dis < d:
                    d = dis
                    p2 = r
        p.append(p2)
        counter +=1
        eliminated +=1
        c = (len(city)) - eliminated
        left = []
        for i in range(c):
            left.append([])
        c = 0
        for r in range(n):
            if r not in p:
                left[c].append(city[r][0])
                left[c].append(city[r][1])
                c +=1
    points1 = [[city[p[0]][0], city[p[0]][1]],[left[0][0],left[0][1]]]
    points2 = [[city[p[1]][0], city[p[1]][1]],[left[0][0],left[0][1]]]
    points3 = [[city[p[0]][0], city[p[0]][1]],[left[1][0],left[1][1]]]
    points4 = [[city[p[1]][0], city[p[1]][1]],[left[1][0],left[1][1]]]
    d1 = distance(points1)
    d2 = distance(points2)
    d3 = distance(points3)
    d4 = distance(points4)
    if (d1-d2)**2 < (d3 - d4)**2:
        print("The central most city is at "+str(left[0][0])+", "+str(left[0][1]))
    elif (d1 - d2)**2 > (d3 - d4)**2:
        print("The central most city is at "+str(left[1][0])+", "+str(left[1][1]))

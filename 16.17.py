import math

# Return the points that form a convex hull 
def getConvexHull(p):   
    # Step 1
    placeP0(p)
    
    # Step 2
    sort(p)
    
    
    stack = [p[0], p[1], p[2]] # We use a list for stack
    
    i = 3
    while i < len(p):
        t2 = stack[len(stack) - 1]
        t1 = stack[len(stack) - 2]
        stack.append(p[i])
        i += 1

    return stack
  
# Return the rightmost lowest point in S 
def getRightmostLowestPoint(p):
    rightMostIndex = 0;
    rightMostX = p[0][0];
    rightMostY = p[0][1];
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i   
    
    return p[rightMostIndex]
  
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
  
# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
def whichSide(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

# Place the rightmost lowest point as the first element in p 
def placeP0(p):
    rightMostIndex = 0
    rightMostX = p[0][0]
    rightMostY = p[0][1]
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i     
    
    # Swap p.get(rightMostIndex) with p[0]
    if rightMostIndex != 0:
        p[0], p[rightMostIndex] = p[rightMostIndex], p[0]

# Sort points
def sort(list):
    for i in range(1, len(list) -1 ):
        # Find the minimum in the list[i..len(list)-1]
        currentMin = list[i]
        currentMinIndex = i

        for j in range(i + 1, len(list)):
            if compareAngles(list[0][0], list[0][1], currentMin[0], currentMin[1], list[j][0], list[j][1]) < 0:
                currentMin = list[j]
                currentMinIndex = j

        # Swap list[i] with list[currentMinIndex] if necessary;
        if (currentMinIndex != i):
            list[currentMinIndex] = list[i]
            list[i] = currentMin

# Compare two points' angles
def compareAngles(x0, y0, x1, y1, x2, y2):
      status = whichSide(x0, y0, x1, y1, x2, y2);        
      if status > 0: # Left side of the line from rightMostLowestPoint to o
        return 1
      elif status == 0:
        return 0
      else:
        return -1


s = input("Enter points: ").split()

p  = []

for i in range(len(s)//2):
    p.append([])
    p[i].append(eval(s[0 + (i*2)]))
    p[i].append(eval(s[1 + (i*2)]))
p = getConvexHull(p)

import turtle

t = turtle
for i in range(len(p)):
    t.penup()
    t.goto(p[i][0], p[i][1])
    t.pendown()
    t.dot(5, "black")

for i in range(len(p)):
    if i == 0:
        t.penup()
        t.goto(p[i][0], p[i][1])
        t.pendown()
    else:
        t.goto(p[i][0], p[i][1])
t.goto(p[0][0], p[0][1])
t.ht()

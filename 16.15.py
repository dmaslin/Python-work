import math
from tkinter import *

class Graham:
    def __init__(self):
        points = [[30, 24],[25, 20],[15, 33],[55, 60],[60, 24],[55, 90]]

        p = self.getConvexHull(points)
        self.p = p
        self.points = points
        window = Tk()
        window.title("Convex Hull using Graham Algorithm")
        c = Canvas(window, height = 100, width = 200, bg = "white")
        c.grid(row = 1, column = 1, sticky = W)
        c.create_rectangle(10, 10, 190, 90, outline = "red")
        c.create_text(100, 30, text = "INSTRUCTIONS")
        c.create_text(100, 50, text = "Add:\tLeft Click")
        c.create_text(100, 70, text = "Remove:\tRight click")
        self.canvas = Canvas(window, height = 100, width = 200, bg = "white")
        self.canvas.grid(row = 1, column = 2, sticky = W)
        for i in range(len(p) - 1):
            self.canvas.create_polygon(p[0 + (1*i)][0], p[0 + (1*i)][1], p[1 + (1*i)][0], p[1 + (1*i)][1], p[0][0], p[0][1], fill = "grey")
        for i in range(len(points)):
            self.canvas.create_oval(points[i][0] - 3, points[i][1] - 3, points[i][0] + 3, points[i][1] +3, fill = "red")
        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-3>", self.remove)
        window.mainloop()
    # Return the points that form a convex hull 
    def getConvexHull(self, p):   
        # Step 1
        self.placeP0(p)
        
        # Step 2
        self.sort(p)
        
        p = self.discardTies(p) # If two points have the same angle, discard the one that is closer to p0
        
        if len(p) < 3:
          return None
        
        stack = [p[0], p[1], p[2]] # We use a list for stack
        
        i = 3
        while i < len(p):
            t2 = stack[len(stack) - 1]
            t1 = stack[len(stack) - 2]
          
            if self.whichSide(t1[0], t1[1], t2[0], t2[1], p[i][0], p[i][1]) <= 0: # on the right of the line from t1 to t2
                # pop the top element off the stack
                stack.pop()
            else:
                # push a new element to the stack
                stack.append(p[i])
                i += 1

        return stack
      
    # Return the rightmost lowest point in S 
    def getRightmostLowestPoint(self, p):
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
        
        return p[rightMostIndex]
      
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
      
    # Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
    def whichSide(self, x0, y0, x1, y1, x2, y2):
        return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

    # Place the rightmost lowest point as the first element in p 
    def placeP0(self, p):
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
    def sort(self, list):
        for i in range(1, len(list) -1 ):
            # Find the minimum in the list[i..len(list)-1]
            currentMin = list[i]
            currentMinIndex = i

            for j in range(i + 1, len(list)):
                if self.compareAngles(list[0][0], list[0][1], currentMin[0], currentMin[1], list[j][0], list[j][1]) < 0:
                    currentMin = list[j]
                    currentMinIndex = j

            # Swap list[i] with list[currentMinIndex] if necessary;
            if (currentMinIndex != i):
                list[currentMinIndex] = list[i]
                list[i] = currentMin

    # Compare two points' angles
    def compareAngles(self, x0, y0, x1, y1, x2, y2):
          status = self.whichSide(x0, y0, x1, y1, x2, y2);        
          if status > 0: # Left side of the line from rightMostLowestPoint to o
            return 1
          elif status == 0:
            return 0
          else:
            return -1

    # If two points have the same angle, discard the one that is closer to p0
    def discardTies(self, p):
        list = [p[0]]
        
        i = 1
        while i < len(p):        
            d = self.distance(p[0][0], p[0][1], p[i][0], p[i][1])
            indexOfLargest = i
            k = i + 1
            while k < len(p) and self.compareAngles(p[0][0], p[0][1], p[i][0], p[i][1], p[k][0], p[k][1]) == 0:
                if (d < self.distance(p[0][0], p[0][1], p[k][0], p[k][1])):
                    d = self.distance(p[0][0], p[0][1], p[k][0], p[k][1])
                    indexOfLargest = k

                k += 1
          
            list.append(p[indexOfLargest])
            i = k
        
        return list
    def refresh(self):
        p = self.p
        points = self.points
        
        self.canvas.delete(ALL)
        p = self.getConvexHull(self.points)
        self.p = p
        self.points = points
        for i in range(len(p) - 1):
            self.canvas.create_polygon(p[0 + (1*i)][0], p[0 + (1*i)][1], p[1 + (1*i)][0], p[1 + (1*i)][1], p[0][0], p[0][1], fill = "grey")
        for i in range(len(points)):
            self.canvas.create_oval(points[i][0] - 3, points[i][1] - 3, points[i][0] + 3, points[i][1] +3, fill = "red")

    def add(self, event):
        self.points.append([])
        a = len(self.points) -1
        self.points[a].append(event.x)
        self.points[a].append(event.y)
        self.refresh()
    def remove(self, event):
        if len(self.points) > 3:
            inPoints = False
            for m in range(len(self.points)):
                if ((event.x - self.points[m][0])**2 + (event.y - self.points[m][1])**2 )**.5 <= 3:
                    inPoints = True
                    self.points.pop(m)
                    self.refresh()
                    break
            if inPoints == False:
                self.points.pop(0)
                self.refresh()
Graham()

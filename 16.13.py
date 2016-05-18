import math
from tkinter import *
class drawPolygon:
    def __init__(self):
        points = [[30, 24],[25, 20],[15, 33],[55, 60],[60, 24],[55, 90]]

        p = self.getConvexHull(points)
        self.p = p
        self.points = points
        window = Tk()
        window.title("Convex Hull using Gift-Wrapping Algorithm")
        c = Canvas(window, height = 100, width = 200, bg = "white")
        c.grid(row = 1, column = 1)
        c.create_rectangle(10, 10, 190, 90, outline = "red")
        c.create_text(100, 30, text = "INSTRUCTIONS")
        c.create_text(100, 50, text = "Add:\tLeft Click")
        c.create_text(100, 70, text = "Remove:\tRight click")
        self.canvas = Canvas(window, height = 100, width = 200, bg = "white")
        self.canvas.grid(row = 1, column = 2)
        for i in range(len(p) - 1):
            self.canvas.create_polygon(p[0 + (1*i)][0], p[0 + (1*i)][1], p[1 + (1*i)][0], p[1 + (1*i)][1], p[0][0], p[0][1], fill = "grey")
        for i in range(len(points)):
            self.canvas.create_oval(points[i][0] - 3, points[i][1] - 3, points[i][0] + 3, points[i][1] +3, fill = "red")
        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-3>", self.remove)
        window.mainloop()
    def getConvexHull(self, myPoints):   
        # Step 1
        h0 = self.getRightmostLowestPoint(myPoints)
        
        H = [h0]    
        t0 = h0
            
        # Step 2 and Step 3
        while True:   
            t1 = myPoints[0]
            for i in range(1, len(myPoints)):
                status = self.whichSide(t0[0], t0[1], t1[0], t1[1], myPoints[i][0], myPoints[i][1])
            
                if status < 0:  # Right side of the line
                    t1 = myPoints[i]
                elif status == 0:
                    if self.distance(myPoints[i][0], myPoints[i][1], t0[0], t0[1]) > self.distance(t1[0], t1[1], t0[0], t0[1]):
                        t1 = myPoints[i]
          
            if t1[0] == h0[0] and t1[1] == h0[1]: 
                break; # A convex hull is found
            else:
                H.append(t1)
                t0 = t1
        return H
      
    # Return the rightmost lowest point in S 
    def getRightmostLowestPoint(self, p):
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
      
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
      
    # Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
    def whichSide(self, x0, y0, x1, y1, x2, y2):
        return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
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
            coord = []
            coord.append(event.x)
            coord.append(event.y)
            inPoints = False
            for m in range(len(self.points)):
                if ((coord[0] - self.points[m][0])**2 + (coord[1] - self.points[m][1])**2 )**.5 <= 3:
                    inPoints = True
                    self.points.pop(m)
                    self.refresh()
                    break
            if inPoints == False:
                self.points.pop(0)
                self.refresh()

drawPolygon()

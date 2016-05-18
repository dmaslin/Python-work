from tkinter import *
import math

class PieChart:
    def __init__(self, parent, data, width = 400, height = 300):
        window = Tk()
        window.title("Pie Chart")
        self.__data = data
        self.__parent = parent
        self.__width = width
        self.__height = height
        self.canvas = Canvas(height = self.__height, width = self.__width, bg = "white")
        self.canvas.pack()

        self.radius = self.__width / 2
        self.radius -= 50
        self.radius = self.radius/2

        parentTotal = 0
        for i in range(len(self.__parent)):
            parentTotal += self.__parent[i][0]
        dataTotal = 0
        for j in range(len(self.__data)):
            dataTotal += self.__data[j][0]
        startingp = 0
        for a in range(len(self.__parent)):
            e = 360 * (self.__parent[a][0]/ parentTotal)
            self.drawAPie(5, 5, startingp, e, self.__parent[a][2], self.__parent[a][1])
            startingp+= e
        startingp = 0
        x1 = self.__width/2+30
        for a in range(len(self.__data)):
            e = 360 * (self.__data[a][0]/ dataTotal)
            self.drawAPie(x1, 5, startingp, e, self.__data[a][2], self.__data[a][1], 2*self.radius - 30)
            startingp+= e

        
            
        window.mainloop()

    def getParent(self):
        return self.__parent
    def getData(self):
        return self.__data
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height

    def setParent(self, parent):
        self.__parent = parent
    def setData(self, data):
        self.__data = data
    def setWidth(self, width):
        self.__width = width
    def setHeight(self, height):
        self.__height = height

    def drawAPie(self,a, b, start, extent, color, title, addToX = 0):
        print(a)
        print(b)
        print(self.radius*2)
        self.canvas.create_arc(a, b, a + self.radius*2, b + self.radius*2, start = start, extent = extent, fill = color)
        x = (a + self.radius*2) / 2 + self.radius * math.cos(math.radians(extent / 2 + start))
        y = (b + self.radius*2) / 2 - self.radius * math.sin(math.radians(extent / 2 + start))
        self.canvas.create_text(x+addToX, y, text = title)


data = [[40, "CS", "red"],[30,"IS","blue"],[50, "IT", "yellow"]]
parent = [[140, "Freshman", "red"], [130,"Sophmore","blue"],[150, "Junior","yellow"],[80,"Senior","green"]]
PieChart(data, parent, 400, 300)

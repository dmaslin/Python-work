import math
from tkinter import *

class RegularPolygonCanvas:
    def __init__(self, width = 400, height = 400):
        window = Tk()
        window.title("n-Sided ")
        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(frame, height = 400, width = 400, bg = "white")
        self.canvas.grid(columnspan = 14)
        Button(frame, text = "-1", command = self.decrease).grid(row = 2, column = 7)
        Button(frame, text = "+1", command = self.increase).grid(row = 2, column = 8)
        self.canvas.bind("<Up>", self.increaseEvent)
        self.canvas.bind("<Down>", self.decreaseEvent)
        self.canvas.focus_set()
        numberOfSides = 4
        self.__width = 400
        self.__height = 400
        self.setNumberOfSides(numberOfSides)
        
    def getNumberOfSides(self):
        return self.__numberOfSides 

    def setNumberOfSides(self, numberOfSides = 4):
        self.__numberOfSides = numberOfSides
        self.drawPolygon()
    def decrease(self):
        if self.__numberOfSides >3:
            self.__numberOfSides -= 1
            self.drawPolygon()
    def increase(self):
        self.__numberOfSides += 1
        self.drawPolygon()
    def decreaseEvent(self, event):
        if self.__numberOfSides >3:
            self.__numberOfSides -= 1
            self.drawPolygon()
    def increaseEvent(self, event):
        self.__numberOfSides += 1
        self.drawPolygon()
        
    def drawPolygon(self):
        self.canvas.delete("polygon")
        
        width = self.__width
        height = self.__height
        xCenter = width / 2
        yCenter = height / 2;
        radius = min(width, height) * 0.4

        angle = 2 * math.pi / self.__numberOfSides
    
        # Create a Polygon object
        polygon = []

        # Add points to the polygon
        for i in range(self.__numberOfSides):
            polygon.append([xCenter + radius * math.cos(i * angle),
                           yCenter - radius * math.sin(i * angle)])     
 
        # Draw the polygon
        self.canvas.create_polygon(polygon, fill = "red", tags = "polygon")
RegularPolygonCanvas()

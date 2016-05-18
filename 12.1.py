import math, turtle
class Triangle:
    def __init__(self, side1 = 1, side2 = 1, side3 = 1, filled = 0, fill = "white"):
        self.filled = fill
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.fill = fill
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getFilled(self):
        return self.filled
    def getFill(self):
        return self.fill

    def setSide1(self, side1):
        self.side1 = side1
    def setSide2(self, side2):
        self.side2 = side2
    def setSide3(self, side3):
        self.side3 = side3
    def setFilled(self, filled):
        self.filled = filled
    def setFill(self, fill):
        self.fill = fill

    def getPerimeter(self):
        p = self.side1 + self.side2 + self.side3
        return p
        
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2;
        temp = s * (s - self.side1) * (s - self.side2) * (s - self.side3)
        area = temp ** 0.5

        if temp < 0 or temp <= 0.0000000000001: return None
        else:
            return area
        
    def isFilled(self):
        if self.filled == 1:
            return True
        elif self.filled == 0:
            return False

    def triangleAngle(a, b, c):
        """Return the angle (in degrees) opposite the side of length a in the
        triangle with sides a, b, c."""
        # See http://en.wikipedia.org/wiki/Law_of_cosines
        return math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2.0 * b * c)))
    
    def drawTriangle(self):
        t = turtle
        if self.filled == 1:
            t.color(self.fill)
            t.begin_fill()
            t.forward(self.side3)
            t.left(180 - self.triangleAngle(self.side2, self.side3, self.side1))
            t.forward(self.side1)
            t.left(180 - self.triangleAngle(self.side3, self.side1, self.side2))
            t.forward(self.side2)
            t.end_fill()
            t.ht()
            t.done()
        elif self.filled == 0:
            t.forward(self.side3)
            t.left(180 - self.triangleAngle(self.side2, self.side3, self.side1))
            t.forward(self.side1)
            t.left(180 - self.triangleAngle(self.side3, self.side1, self.side2))
            t.forward(self.side2)
            t.ht()
            t.done()
        print("Your Triangle")
        print(self.__str__())
        print("Color = "+self.fill)
        print("Filled = "+str(self.isFilled()))
        print("The perimeter is "+str(self.getPerimeter()))
        print("The area is "+str(self.getArea()))

    def __str__(self):
        return "Triangle: side 1 = "+str(side1)+" side 2 = "+str(side2)+" side 3 = "+str(side3)
    

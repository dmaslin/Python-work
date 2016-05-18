import triangle

a, b, c = eval(input("Enter the lenths of the triangle sides: "))
color = input("What color should it be: ")
filled = eval(input("Do you want the triangle filled with your color you chosen (enter 0 for no 1 for yes): "))
import turtle
t = triangle.Triangle(a, b, c, filled, color)

t.drawTriangle()

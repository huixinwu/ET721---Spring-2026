"""
student's full name
lab 6, classes, object, and methods
"""
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]


print("\n ---- example 1: classes ")
# a class is like a blueprint of something
# using the class, we can create different instance of an object
# data attributes (properties) are values that represents an object
# methods are functions of an object


class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color
    
    # method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r

class Rectangle(object):
    def __init__(self, heigth, width, color):
        self.h = heigth
        self.w = width
        self.c = color
    
    # method to calculate and return the area of the rectangle
    def area(self):
        return self.h * self.w
    
    # method to calculate the perimeter of a rectangle
    def perimeter(self):
        return 2*self.w + 2*self.h

    # method to draw the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fc=self.c))
        plt.axis("scaled")
        plt.show()


# create an instance of an object
circle1 = Circle(5,"yellow")
circle2 = Circle(2, "red")

rectangle1 = Rectangle(2, 3, "green")
rectangle2 = Rectangle(5, 4, "blue")

# accessing to data in an object
print(f"color of circle 2 = {circle2.c}")
print(f"The area of rectangle 1 = {rectangle1.w * rectangle1.h}")
print(f"The area of rectangle 2 = {rectangle2.w * rectangle2.h}")

# modify data of an object
circle2.c = "orange"
print(f"color of circle 2 after modification = {circle2.c}")

print(f"radius of circle 2 = {circle2.r}")
# call method add_radius in circle2 and pass 6
circle2.add_radius(6)
print(f"radius of circle 2 after method add_radius = {circle2.r}")

# call methods in class Rectangle
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The perimeter of rectangle 2 = {rectangle2.perimeter()}")

# draw rectangle
rectangle2.drawRectangle()

print("\n EXERCISE")
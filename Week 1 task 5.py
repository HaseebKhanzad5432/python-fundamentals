import math

# Parent Class
class Shape:
    def area(self):
        print("Area is not defined.")

# Child Class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Child Class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Creating Objects
circle = Circle(5)
rectangle = Rectangle(10, 4)

# Display Areas
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())

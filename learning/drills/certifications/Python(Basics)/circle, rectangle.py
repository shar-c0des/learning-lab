import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Read the number of queries
q = int(input())

for _ in range(q):
    # Split the input line into parts
    parts = input().split()
    shape = parts[0]

    if shape == "circle":
        radius = float(parts[1])
        circle_obj = Circle(radius)
        area = circle_obj.area()
        print("{0:.2f}".format(area))
    elif shape == "rectangle":
        length = float(parts[1])
        width = float(parts[2])
        rectangle_obj = Rectangle(length, width)
        area = rectangle_obj.area()
        print("{0:.2f}".format(area))
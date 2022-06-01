from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def get_area(self):
        return 1/2 * self.base * self.height

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
    def get_area(self):
        return self.lenght**2

from math import pi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return pi * self.radius**2

triangle = Triangle(6, 3)
square = Square(4)
circle = Circle(5)

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area())
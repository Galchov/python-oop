from abc import ABC, abstractmethod
from math import pi


# Using 'abc' library to inherit from 'ABC' class, which makes my class abstract.
class Shape(ABC):

    # Abstract method, which means it must be defined by the children classes.
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # A=wl
    def calculate_area(self):
        return self.width * self.height

    # P=2(l+w)
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # A=πr2
    def calculate_area(self):
        return pi * self.radius * self.radius

    # C=2πr
    def calculate_perimeter(self):
        return 2 * pi * self.radius


# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())

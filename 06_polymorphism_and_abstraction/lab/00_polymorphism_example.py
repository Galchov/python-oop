"""
In this particular example we can see how the Polymorphism works in the OOP.
Two instance methods (get_area & get_perimeter) declared in the super class
are being redefined in all the subclasses and given different functionality
based on the child class requirements. This is known as Method Overriding.

The method's names must not be changed when redefined in the subclasses!
"""

from math import pi


class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_area(self) -> None:
        pass

    def get_perimeter(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"I am {self.name}"


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        super().__init__("Circle")
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, length: int) -> None:
        super().__init__("Square")
        self.length = length

    def get_area(self) -> int:
        return self.length ** 2

    def get_perimeter(self) -> int:
        return self.length * 4

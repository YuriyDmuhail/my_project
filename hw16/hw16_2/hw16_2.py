from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Triangle(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.__side ** 2

    def perimeter(self):
        return 3 * self.__side


figures = [
    Circle(5),
    Rectangle(4, 7),
    Triangle(6)
]

for figure in figures:
    print(f"{figure.__class__.__name__}:, Площа: {figure.area():.2f}")
    print(f"  Площа: {figure.area():.2f}")
    print(f"  Периметр: {figure.perimeter():.2f}")




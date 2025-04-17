# Abstraction in Python using Abstract Base Classes (ABC)
from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        return "This is a geometric shape"


# Concrete classes implementing the abstract class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"


# Cannot instantiate abstract class
# shape = Shape()  # This will raise TypeError

# Creating objects of concrete classes
rectangle = Rectangle(5, 4)
circle = Circle(7)

# Using the objects
# print(rectangle.description())
# print(f"Rectangle Area: {rectangle.area()}")
# print(f"Rectangle Perimeter: {rectangle.perimeter()}")
# print(rectangle)

# print("\n" + circle.description())
# print(f"Circle Area: {circle.area()}")
# print(f"Circle Perimeter: {circle.perimeter()}")
# print(circle)

# 2. Cree una clase abstracta de `Shape` que:
#    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#    2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#   3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass
    
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    
    def calculate_perimeter(self) -> float:
        return 4 * self.side
    
    def calculate_area(self) -> float:
        return self.side ** 2
    
    def __str__(self):
        return f"Square with side {self.side}"


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def calculate_area(self) -> float:
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"


if __name__ == "__main__":
    shapes = [
        Circle(5),
        Square(4),
        Rectangle(3, 6)
    ]
    
    for shape in shapes:
        print(f"{shape}:")
        print(f"  Perimeter: {shape.calculate_perimeter():.2f}")
        print(f"  Area: {shape.calculate_area():.2f}")
        print()

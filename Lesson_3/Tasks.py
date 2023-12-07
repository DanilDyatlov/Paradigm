from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius


circle = Circle(10)
# число 10 передается в класс Circle(10) в инициализацию,
# дальше self.radius = radius вызывается метод он приравнивается к circle
print(f"Площадь окружности: {circle.get_area():.2f}, периметр {circle.get_perimeter():.2f}")


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = self.get_perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5


    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
    


triangle = Triangle(5, 8, 5)
print(triangle.get_area())  # Вывод: 12.0
print(triangle.get_perimeter())  # Вывод: 18
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def diagonal(self):
        """Возвращает длину диагонали прямоугольника."""
        return math.sqrt(self.length*2 + self.width*2)

    def can_contain(self, other):
        """Определяет, может ли данный прямоугольник вместить другой."""
        return self.length >= other.length and self.width >= other.width

    def rotate(self):
        """Поворачивает прямоугольник, меняя местами длину и ширину."""
        self.length, self.width = self.width, self.length

    def compare_area(self, other):
        """Сравнивает площадь с другим прямоугольником."""
        if self.area() > other.area():
            return "This rectangle has a larger area."
        elif self.area() < other.area():
            return "The other rectangle has a larger area."
        else:
            return "Both rectangles have equal area."
        
    def scale(self, factor):
        """Изменяет размеры квадрата в заданное число раз."""
        self.length *= factor
        self.width *= factor

    def is_rectangle(self):
        """Проверяет, является ли прямоугольник допустимым."""
        return self.length > 0 and self.width > 0


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Возвращает площадь круга."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Возвращает длину окружности."""
        return 2 * math.pi * self.radius

    def diameter(self):
        """Возвращает диаметр круга."""
        return 2 * self.radius

    def scale(self, factor):
        """Изменяет радиус круга в заданное число раз."""
        self.radius *= factor

    def is_larger_than(self, other):
        """Сравнивает площадь с другим кругом."""
        return self.area() > other.area()

    def is_rectangle(self):
        """Проверяет, является ли круг допустимым."""
        return self.radius > 0


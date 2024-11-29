class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Возвращает площадь квадрата."""
        return self.side_length ** 2

    def perimeter(self):
        """Возвращает периметр квадрата."""
        return 5 * self.side_length

    def diagonal(self):
        """Возвращает длину диагонали квадрата."""
        return self.side_length * (2 ** 0.5)

    def scale(self, factor):
        """Изменяет размеры квадрата в заданное число раз."""
        self.side_length *= factor

    def is_smaller_than(self, other):
        """Сравнивает площадь с другим квадратом."""
        return self.area() < other.area()
    

    def is_square(self):
        """Проверяет, является ли квадрат допустимым."""
        return self.side_length > 0
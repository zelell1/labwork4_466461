class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        """Возвращает периметр треугольника."""
        return self.a + self.b + self.c

    def area(self):
        """Возвращает площадь, используя формулу Герона."""
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_equilateral(self):
        """Проверяет, является ли треугольник равносторонним."""
        return self.a == self.b == self.c

    def scale(self, factor):
        """Изменяет размеры треугольника в заданное число раз."""
        self.a *= factor
        self.b *= factor
        self.c *= factor

    def is_trinagle(self):
        """Проверяет, является ли треугольник допустимым."""
        return (self.a + self.b > self.c and
                self.b + self.c > self.a and
                self.c + self.a > self.b)
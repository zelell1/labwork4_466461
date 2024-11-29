import unittest
from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle

class TestGeometricShapes(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(radius=4)
        self.square = Square(side_length=5)
        self.rectangle = Rectangle(length=5, width=11)
        self.triangle = Triangle(a=3, b=4, c=5)  # Используем только стороны

    # Circle tests
    def test_circle_area(self):
        self.assertAlmostEqual(self.circle.area(), 50.2654824574, places=4)

    def test_circle_circumference(self):
        self.assertAlmostEqual(self.circle.circumference(), 25.1327412287, places=4)

    def test_circle_zero_radius(self):
        circle = Circle(radius=0)
        self.assertEqual(circle.area(), 0)
        self.assertEqual(circle.circumference(), 0)

    # Square tests
    def test_square_area(self):
        self.assertEqual(self.square.area(), 20)

    def test_square_perimeter(self):
        self.assertEqual(self.square.perimeter(), 20)

    def test_is_square(self):
        sq = Square(side_length=-4).is_square()
        self.assertFalse(sq)
            

    def test_square_zero_side(self):
        square = Square(side_length=0)
        self.assertEqual(square.area(), 0)
        self.assertEqual(square.perimeter(), 0)

    # Rectangle tests
    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 55)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 32)

    def test_rectangle_invalid_dimensions(self):
        a = Rectangle(length=-5, width=10)
        self.assertFalse(a.is_rectangle())

    def test_rectangle_zero_side(self):
        rectangle = Rectangle(length=0, width=5)
        self.assertEqual(rectangle.area(), 0)
        self.assertEqual(rectangle.perimeter(), 10)

    # Triangle tests
    def test_triangle_area(self):
        # Используем формулу Герона для площади треугольника
        self.assertAlmostEqual(self.triangle.area(), 6, places=1)

    def test_triangle_perimeter(self):
        self.assertEqual(self.triangle.perimeter(), 12)

    def test_triangle_invalid_sides(self):
        tr = Triangle(a=1, b=2, c=10)
        self.assertFalse(tr.is_trinagle())

    def test_triangle_validity(self):
        self.assertTrue(self.triangle.is_trinagle())

    def test_triangle_zero_sides(self):
        Triangle(a=0, b=0, c=0)

    def test_equilateral_triangle(self):
        triangle = Triangle(a=5, b=5, c=5)
        self.assertTrue(triangle.is_equilateral())

    def test_scaling_shapes(self):
        self.circle.scale(2)
        self.assertAlmostEqual(self.circle.radius, 8)

        self.square.scale(2)
        self.assertEqual(self.square.side_length, 10)

        self.rectangle.scale(2)
        self.assertEqual(self.rectangle.length, 10)
        self.assertEqual(self.rectangle.width, 22)


if __name__ == '__main__':
    unittest.main()
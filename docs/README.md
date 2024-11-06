# Geometric Library

## Overview

This library provides a set of classes for handling geometric operations for four common shapes: Circle, Square, Rectangle, and Triangle. With these classes, you can easily calculate properties such as area, perimeter (or circumference in the case of a circle), and more.

## Installation

To use this library, simply clone the repository to your local system, and import the necessary classes into your Python project.

git clone <https://github.com/zelell1/labwork4_466461>
## Usage

Below is a brief guide on how to utilize each class in this library.

-- Circle

The Circle class allows you to perform various calculations given the radius.

circle = Circle(radius=4)
print("Area:", circle.area())              # Output: ~50.27
print("Circumference:", circle.circumference())  # Output: ~25.13
print("Diameter:", circle.diameter())      # Output: 8
circle.scale(2)
print("New Radius:", circle.radius)        # Output: 8
-- Square

The Square class provides methods for various calculations using the side length.

square = Square(side_length=5)
print("Area:", square.area())              # Output: 25
print("Perimeter:", square.perimeter())    # Output: 20
print("Diagonal:", square.diagonal())      # Output: ~7.07
square.scale(2)
print("New Side Length:", square.side_length) # Output: 10
-- Rectangle

The Rectangle class can be used to calculate a variety of properties with the given length and width.

rectangle = Rectangle(length=5, width=11)
print("Area:", rectangle.area())           # Output: 55
print("Perimeter:", rectangle.perimeter()) # Output: 32
print("Diagonal:", rectangle.diagonal())   # Output: ~11.18
rectangle.rotate()
print("New Dimensions:", rectangle.length, rectangle.width) # Output: 11, 5
-- Triangle

The Triangle class includes methods for various calculations using the side lengths.

triangle = Triangle(a=3, b=4, c=5)
print("Area:", triangle.area())            # Output: 6.0
print("Perimeter:", triangle.perimeter())  # Output: 12
print("Is Equilateral:", triangle.is_equilateral()) # Output: False
triangle.scale(2)
print("New Side Lengths:", triangle.a, triangle.b, triangle.c) # Output: 6, 8, 10
## Class Descriptions

Each class is equipped with methods to perform fundamental geometric calculations. The parameters are expected to be numeric (float or int).

- Circle
  - area(): Calculates the area.
  - circumference(): Calculates the circumference.
  - diameter(): Returns the diameter.
  - scale(factor): Scales the circle by the given factor.
  - is_larger_than(other): Compares the area with another circle.
  - is_rectangle(): Checks if the circle is valid.

- Square
  - area(): Calculates the area.
  - perimeter(): Calculates the perimeter.
  - diagonal(): Calculates the diagonal.
  - scale(factor): Scales the square by the given factor.
  - is_smaller_than(other): Compares the area with another square.
  - is_square(): Checks if the square is valid.

- Rectangle
  - area(): Calculates the area.
  - perimeter(): Calculates the perimeter.
  - diagonal(): Calculates the diagonal.
  - can_contain(other): Checks if the rectangle can contain another.
  - rotate(): Rotates the rectangle.
  - compare_area(other): Compares the area with another rectangle.
  - scale(factor): Scales the rectangle by the given factor.
  - is_rectangle(): Checks if the rectangle is valid.

- Triangle
  - area(): Calculates the area using Heron's formula.
  - perimeter(): Calculates the perimeter.
  - is_equilateral(): Checks if the triangle is equilateral.
  - scale(factor): Scales the triangle by the given factor.
  - is_triangle(): Checks if the triangle is valid.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas for improving the library.

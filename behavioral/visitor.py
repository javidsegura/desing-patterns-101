"""

Intent:
      - Decouples operation definition (and execution). Allows for having object definition separte from class

Note:
      - Difference with bridge: no way to accept different abstractions by visitor. Also, implementations are not classes with several different logic, just one method per item
      - Difference with Command: both do separation logic. Command has support for treating the request
      as an object that can be redone, queued, whereas visitor only has the code execution part + it can execute across a family of objects

Components:
      - Visitor => defines functionality for all elements. Visits element-specific methdos
      - Element => each accepet a visitor (operation visitor)

"""

from abc import abstractmethod, ABC
from typing import List

class Visitor():
      @abstractmethod
      def visit_circle(self, circle: "Circle"):
            pass
      @abstractmethod
      def visit_triangle(self, triangle: "Triangle"):
            pass
      @abstractmethod
      def visit_square(self, circle: "Square"):
            pass
class AreaCalculatorVisitor(Visitor):
      def visit_circle(self, circle: "Circle"):
            print(f"Calculating area of a Circle with radius {circle._radius}")
            return 3.14 * circle._radius ** 2
      def visit_square(self, square: "Square"):
            print(f"Calculating area of a Square with side {square._side}")
            return square._side ** 2

      def visit_triangle(self, triangle: "Triangle"):
            print(f"Calculating area of a Triangle with base {triangle._base} and height {triangle._height}")
            return 0.5 * triangle._base * triangle._height

class Shape(ABC):
      def accept(self, visitor: "Visitor"):
            pass

class Circle(Shape):
      def __init__(self, radius: int) -> None:
            self._radius = radius
      def accept(self, visitor: Visitor):
            return visitor.visit_circle(self)
class Triangle(Shape):
      def __init__(self, base: int, height: int) -> None:
            self._base = base
            self._height = height
      def accept(self, visitor: Visitor):
            return visitor.visit_triangle(self)
class Square(Shape):
      def __init__(self, side: int) -> None:
            self._side = side
      def accept(self, visitor: Visitor):
            return visitor.visit_square(self)


if __name__ == "__main__":
      shapes: List[Shape] = [Circle(5), Square(10), Triangle(4, 6)]
      area_visitor = AreaCalculatorVisitor()

      for shape in shapes:
            shape.accept(area_visitor)
"""
Intent: separating a given abstraction from all its implementations

Components:
      - Abstraction/Subject (the what) (N)=> all subjects inherit this methods
      - Concrete abstraction 
      - Implementation interface/functionality (the how)(M)=> All methods to be followed by implementations (all concrete abstraction should be included here)
      - Concrete  

Usecase:
      - Abstraction (geometrical shapes) & Implementation (Renderer)
      - 2 geom shapes & 2 renderers

Notes:
      - Different to factory, here we are just separate partso of the logic internal to the object. In factory we decouple specific object creation process from how its used (through factories)
      U create an object calling a concrete factory
"""

from abc import ABC, abstractmethod

# --- IMPLEMENTATION ---
class Renderer(ABC): 
      @abstractmethod
      def draw_circle(self, radius):
            pass
      @abstractmethod
      def draw_triangle(self, side):
            pass

class OpenGL(Renderer):
      def draw_circle(self, radius):
            return "Rendering circle with OpenGL"
      def draw_triangle(self, side):
            return "Rendering triangle with OpenGL"
class VectorRenderer(Renderer):
      def draw_circle(self, radius):
            return "Rendering circle with VectorRenderer"
      def draw_triangle(self, side):
            return "Rendering triangle with VectorRenderer"

# --- ABSTRACTION ---
class Shape(ABC): 
      def __init__(self, renderer: Renderer) -> None:
            self._renderer = renderer
      @abstractmethod
      def draw(self):
            ...

class Circle(Shape):
      def __init__(self, radius, renderer: Renderer) -> None:
            super().__init__(renderer)
            self._radius = radius
      def draw(self):
            return self._renderer.draw_circle(self._radius)
class Triangle(Shape):
      def __init__(self, side, renderer: Renderer) -> None:
            super().__init__(renderer)
            self._side = side
      def draw(self):
            return self._renderer.draw_triangle(self._side)

if __name__ == "__main__":
      renderer = OpenGL()
      circle = Circle(radius=2, renderer=renderer)
      print(circle.draw())
      
""" 
We have succesfully achieved via decomposition N (subjects) + M (functionalites) classes, instead of N*M. 
This means we can decouple the code between a an abstraction from its implementation
"""
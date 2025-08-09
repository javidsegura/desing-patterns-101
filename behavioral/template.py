"""
Intent: define methods to be implemented by subclasses. Essentially, creating an interface for an object.

"""
from abc import ABC, abstractmethod

class MyClass(ABC):
      @abstractmethod
      def my_primitive_operation(self):
            pass
      def my_template_method(self):
            print("Im a tempalte method")

class SubClassA(MyClass):
      def my_primitive_operation(self):
            print(f"Primitive operatio from {__class__} ")

class SubClassB(MyClass):
      def my_primitive_operation(self):
            print(f"Primitive operatio from {__class__} ")

if __name__ == "__main__":
      temp = SubClassA()
      foo = SubClassB()
      temp.my_primitive_operation()
      foo.my_primitive_operation()
      temp.my_template_method()
      foo.my_template_method()
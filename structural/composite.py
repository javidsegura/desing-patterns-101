"""
Intent: for tree-like data object it providies a unified interface for the leaf vs the non-leaf nodes

Components:
      - Leaf
      - Composite (collection of objects, non-leaf)
      - Component (unified interface that deals with logic of leaf + composite)

Flow:
      - Client passes a tree-like object to component for the constructor to register it. Then calls extraction on it, and the component handles the extraction for nested 
      or shallow objects

Use case:
      - A box contains another box or an item. Each box has a price + item have their own corresponding price. Return complete price

"""
from abc import abstractmethod, ABC

class Component(ABC):
      @abstractmethod 
      def get_price(self) -> float:
            pass

class Item(Component): # Leaf 
      def __init__(self, name: str, price: float) -> None:
            self._name = name
            self._price = price
      def get_price(self):
            return self._price

class Box(Component):  # Composite
      def __init__(self, box_name: str ,box_price: float = 1) -> None:
            self._box_price = box_price
            self._children = []
      def add(self, component: Component):
            self._children.append(component)
      def remove(self, component: Component):
            self._children.remove(component)
      def get_price(self) -> float:
            total_price = self._box_price
            for children in self._children:
                  children_price = children.get_price()
                  total_price += children_price
            return total_price

if __name__ == "__main__":
    pen = Item("Pen", 2.50)
    notebook = Item("Notebook", 5.00)
    eraser = Item("Eraser", 1.00)
    pencil_case = Item("Pencil Case", 3.50)

    # Create a box for school supplies (Composite)
    school_box = Box("School Supplies Box")
    school_box.add(pen)
    school_box.add(notebook)
    school_box.add(eraser)

    # Create another box for just a pencil set (Composite)
    pencil_set_box = Box("Pencil Set Box")
    pencil_set_box.add(Item("Pencil (HB)", 0.75))
    pencil_set_box.add(Item("Pencil (2B)", 0.75))

    # Add the pencil set box to the school box, demonstrating nesting
    school_box.add(pencil_set_box)
    school_box.add(pencil_case)

    # The top-level container (Composite)
    main_package = Box("Main Shipping Package")
    main_package.add(school_box)
    main_package.add(Item("Textbook", 25.00))

    print("\n--- Calculating total price of the main package ---")
    total_price = main_package.get_price()
    print(f"The total price of the main shipping package is: ${total_price}")

    print("\n--- Calculating total price of just the school box ---")
    school_box_price = school_box.get_price()
    print(f"The price of the 'School Supplies Box' is: ${school_box_price}")

    print("\n--- Calculating price of a single item ---")
    pen_price = pen.get_price()
    print(f"The price of a single 'Pen' is: ${pen_price}")
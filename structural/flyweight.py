

"""

Components:
      - Flyweight: creates charcther. Provides method for displaiyng
      - Flyweight factory: manages map for flyweight creation. Contains list of flyweight objects.
      - Context: character creation shared and internal method invokation, external attributes
      
Usecase:
      - A characther with used attributes being char string
      - Client creates several char from a string, renders all chars 
      - Check flyweights list 

Notes:
      - Create an extrinsic method both with and without the instrict 2
"""

from typing import List

class Flyweight():
      """
      This emulates some  data + methods that are resource-intensive (CPU in computations or memory)
      """
      def __init__(self, char: str) -> None:
            self._char = char

      def display(self, font_size: int, x_coord: int, y_coord: int):
            print(f"- Displaying: {self._char} with font_size: {font_size} and coords: ({x_coord}, {y_coord})")
            
class FlyweightFactory():
      flyweights = {}

      @staticmethod
      def get_flyweight(char: str) -> Flyweight:
            if char in __class__.flyweights:
                  print(f"'{char}' already exisitng")
            else:
                  print(f"'{char}' did not exist")
                  __class__.flyweights[char] = Flyweight(char)
            return __class__.flyweights[char]
      @staticmethod
      def list_flighweight():
            return list(__class__.flyweights.keys())
      
class Charachter():
      def __init__(self, char: str, font_size: int, x_coord: int, y_coord: int) -> None:
            self.flyweight = FlyweightFactory.get_flyweight(char)
            self._char = char
            self._font_size = font_size
            self._x_coord = x_coord
            self._y_coord = y_coord

      def render(self):
            self.flyweight.display(self._font_size, self._x_coord, self._y_coord)

if __name__ == "__main__":
      text = "Hello world! Hope you have a good day!"
      list_of_chars: List[Charachter] = []

      for i, char in enumerate(text):
            list_of_chars.append(Charachter(char, font_size=12, x_coord=i*10, y_coord=50))
      
      print("="*40)

      for char_obj in list_of_chars:
            char_obj.render()
      
      print(FlyweightFactory.list_flighweight())

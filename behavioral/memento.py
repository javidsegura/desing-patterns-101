"""

Intent: saving an object's internal state (e.g., an attribute) without storing its full internal details

Components:
      - Originator => object that has its state stored + has its own independent functionality
      - Memento => save a state  
      - Caretaker => stores all mementos. Can have undoing functionality

Usecase:
      - A texteditor that keeps track of the content state
"""

from abc import ABC, abstractmethod

class Memento():
      def __init__(self, content) -> None:
            self._content = content
      def get_content(self):
            return self._content

class TextEditor(): # Originator
      def __init__(self) -> None:
            self._content = ""
      def write(self, text):
            self._content += text
      def get_content(self):
            return self._content
      def save(self):
            return Memento(self._content)
      def restore(self, memento: Memento):
            self._content = memento.get_content()

class Mediator():
      def __init__(self) -> None:
            self._mementos = []
      def save_state(self, memento: Memento):
            self._mementos.append(memento)
      def undo(self):
            if self._mementos:
                  self._mementos.pop()
                  return self._mementos[-1]

if __name__ == "__main__":
      word = TextEditor()
      history = Mediator()
      word.write("Hello world!")
      history.save_state(word.save())
      word.write("How are you doing?")
      print(f"Current content is: {word.get_content()}")
      history.save_state(word.save())
      word.restore(history.undo())
      print(f"Current content is: {word.get_content()}")
      

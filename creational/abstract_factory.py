"""
Intent: create families of related objects 

Components:
      - Abstract factory
      - Concrete factory 
      - Abstract product 
      - Concrete product

Flow:
      - Client decides abstract factory 

Use-case scenario:
      - Dark/light UI theming as abstract factory. Button and checkbox as elements 

"""

from abc import ABC, abstractmethod

# -- ABSTRACT PRODUCTS -- 
class Button(ABC): 
      @abstractmethod
      def click(self):
            pass

class CheckBox(ABC): 
      @abstractmethod
      def toggle(self):
            pass

# -- CONCRETE PRODUCTS -- 
class LightButton(Button):
      def click(self):
            print("Clicking a light button")
class DarkButton(Button):
      def click(self):
            print("Clicking a dark button")

class LightCheckbox(ABC):
      def toggle(self):
            print("Toggling a light checkbox")
class DarkCheckbox(ABC):
      def toggle(self):
            print("Toggling a dark checkbox")

# -- ABSTRACT FACTORY --
class GUIFactory(ABC):
      @abstractmethod
      def create_button(self) -> Button:
            pass
      @abstractmethod
      def create_checkbox(self) -> CheckBox:
            pass

# -- CONCRETE FACTORIES -- 
class LightThemeFactory(GUIFactory):
      def create_button(self):
            return LightButton()
      def create_checkbox(self ):
            return LightCheckbox()
      
class DarkThemeFactory(GUIFactory):
      def create_button(self):
            return DarkButton()
      def create_checkbox(self):
            return DarkCheckbox()
      
class Application():
      def __init__(self, theme: GUIFactory) -> None:
            self._theme = theme
            self._button = None
            self._checkbox = None

      def create_ui(self):
            self._button = self._theme.create_button()
            self._checkbox = self._theme.create_checkbox()

      def interact(self):
            if self._button:
                  self._button.click()
            if self._checkbox:
                  self._checkbox.toggle()

if __name__ == "__main__":
      theme = DarkThemeFactory()
      app = Application(theme=theme)
      app.create_ui()
      app.interact()
"""

Intent: change an algorithm to be used at run time

Compoentn:
      - Strategies => interface to execute a given 
      - Context => where to use the given strategy

Usecase:
      - Setting some text in a different way
Note:
      - Calling different strategies could be treated as 1:M bridge design pattern 
      - If we parametrize the strategy, we would have a 'simple factory' design pattern
"""
from abc import abstractmethod, ABC

class FormattingStrategy(ABC):
      def format(self, text):
            pass

class PlainTextStrategy(FormattingStrategy):
      def format(self, text):
            return text
class BoldTextStrategy(FormattingStrategy):
      def format(self, text):
            return f"**{text}**"
      
class TextArea(): # Context
      def __init__(self, strategy: FormattingStrategy) -> None:
            self.strategy = strategy
      def set_strategy(self, strategy: FormattingStrategy):
            self.strategy = strategy
      def render(self, text):
            self.strategy.format(text)
      

if __name__ == "__main__":
      mytext = TextArea(PlainTextStrategy())
      content = "Hello World!"
      mytext.render(content)
      mytext.set_strategy(BoldTextStrategy())
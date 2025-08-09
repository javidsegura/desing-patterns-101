"""
Intent: decoupling request sender from its receivers. Allows to limit the cluttering of many steps that review the request object

Components:
      - Handler (Inteface + Concrete) => defines method to pass check + to pass onto the next node 

Flow:
      - A handler receives some data + handler object.
      - Sets two methdos for checking data + passing to the next one
      - Client then sets the chain

Use-case:
      - Data validation: 3 different validators: size, data type and allowed chars
"""

from abc import abstractmethod, ABC
from typing import Any

class Validator(ABC):
      next_validator = None

      @abstractmethod
      def handle(self, data: Any):
            """ 
            You cant have the abstract method be defined at the super level and call it from the sublclass if needed (even inside the abstract method)
            """
            if self.next_validator:
                  return self.next_validator.handle(data)
            return None

      def set_next(self, validator: "Validator") -> "Validator":
            self.next_validator = validator
            return validator

class SizeValidator(Validator):
      def __init__(self, max_len: int) -> None:
            self._max_len = max_len
            super().__init__()
      def handle(self, data: Any):
            if len(data) >= self._max_len:
                  return f"Failed at {__class__}"
            return super().handle(data)

class DataTypeValidator(Validator):
      def handle(self, data: Any):
            if not isinstance(data, str):
                  return f"Failed at {__class__}"
            return super().handle(data)

class FormatValidator(Validator):
      def __init__(self, allowed_chars: str) -> None:
            self._allowed_chars = allowed_chars
            super().__init__()
      def handle(self, data: Any):
            for char in data:
                  if char not in self._allowed_chars:
                        return f"Failed at {__class__}. Not allowed char is: {char}"
            return super().handle(data)
      
def process_data_validation(data: Any, validator: Validator):
      error_msg = validator.handle(data)
      if error_msg: 
            print(f"Validation failed: {error_msg} for '{data}'")
      else:
            print(f"Validation has been succesful for '{data}'")
            
if __name__ == "__main__":
      validator = SizeValidator(max_len=20)
      validator.set_next(DataTypeValidator()) \
               .set_next(FormatValidator("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "))
      
      process_data_validation(data="HelloWorld123", validator=validator)
      process_data_validation(data="TooLongStringForTestingValidation", validator=validator)

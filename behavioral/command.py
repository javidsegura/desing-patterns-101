"""
Intent: decoupling command execution from object. Useful for reverting command execution, adding metadata

Components
      - Command => interface for command exections + specifc command 
      - Receiver => object that command executed upon (contain the actual logic/implementation of the method)
      - Invoker => logic for invoking cmds

Usecase:
      - Payment processing with procedural approach: charging, updating stock db, send confirmation email

Note: you can emulate behavior without cmd. However, undo/redo would be tedious, and anything but modulara
"""

from abc import abstractmethod, ABC
import random
from typing import List

# Receiver 
class PaymentGatewayService():
      def charge(self, quantity: int):
            print(f"Charging {quantity}€")
      def reimburse(self, quantity: int):
            print(f"Reimbursing {quantity}€")

class EmailService():
      def send(self, direction: str, message: str):
            print(f"Sending {message} to {direction}")

class InventoryService():
      def reserve(self, ski):
            print(f"Reserving item with ski {ski}")
      def restore(self, ski):
            print(f"Restoring item with ski {ski}")

# Command
class Command(ABC): 
      @abstractmethod
      def execute_method(self):
            pass

      @abstractmethod
      def undo_method(self):
            pass

class PaymentGatewayCommand(Command):
      def __init__(self, pg: PaymentGatewayService, quantity: id) -> None:
            self.pg = pg
            self.quantity = quantity
      def execute_method(self):
            self.pg.charge(self.quantity)
      def undo_method(self):
            self.pg.reimburse(self.quantity)
            
class EmailCommand(Command):
      def __init__(self, es: EmailService, direction: str, message: str) -> None:
            self.es = es
            self.direction = direction
            self.message = message
      def execute_method(self):
            self.es.send(direction=self.direction,
                         message=self.message)
      def undo_method(self):
            print(f"Email cant be undone")

class InventoryCommand(Command):
      def __init__(self, inventory_service: InventoryService, ski: int) -> None:
           self.inventory = inventory_service
           self.ski = ski
      def execute_method(self):
            self.inventory.reserve(self.ski)
      def undo_method(self):
            self.inventory.restore(self.ski)
      
# Invoker 
class Invoker():
      def __init__(self) -> None:
            self.executed: List[Command] = []
      def run(self, command_list: List[Command]):
            for cmd in command_list:
                  try:
                        cmd.execute_method()
                        self.executed.append(cmd)
                        if random.random() >= 0.5: # Fake error in order to test undoing functionality 
                              raise Exception
                  except Exception as e:
                        for cmd in reversed(self.executed):
                              cmd.undo_method()
                        break

if __name__ == "__main__":
      invoker = Invoker()
      invoker.run(
            [      
            PaymentGatewayCommand(PaymentGatewayService(), quantity=12),
            EmailCommand(EmailService(), direction="hello@gmail.com", message="How are you doing?"),
            InventoryCommand(InventoryService(), ski=1212)
            ]
      )
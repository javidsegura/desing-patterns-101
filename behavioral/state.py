"""
Intent: having an object behave differently as its in different phases (with the same methods). Sort of the object being a finite state machine, 
having a possible state for each

Components:
      - Contents => controls the passing between states and their invokation
      - State (interface & concrete implementation) => defines uniform methods for all states


Usecase:
      - A traffic light with three different light states (red, yellow, green). Methods are handle_request + transition_to_next

"""

from abc import ABC, abstractmethod

class LightState(ABC):

      context = None

      @abstractmethod
      def handle_request(self):
            pass
      @abstractmethod
      def transition_to_next_state(self):
            pass

class RedState(LightState):
      def handle_request(self):
            print(f"Red light is being here as of now!")
      def transition_to_next_state(self):
            self.context.transition_to(GreenState())
class YellowState(LightState):
      def handle_request(self):
            print(f"Yellow light is being here as of now!")
      def transition_to_next_state(self):
            self.context.transition_to(RedState())
class GreenState(LightState):
      def handle_request(self):
            print(f"Green light is being here as of now!")
      def transition_to_next_state(self):
            self.context.transition_to(YellowState())

class TrafficLight:

      _state = None

      def __init__(self, state: LightState) -> None:
            self.transition_to(state)
      def transition_to(self, state: LightState): # Called by the states (they need to speicify which state form their object)
            self.state = state
            self.state.context = self
      def request_next(self): # Called by the cliet
            self.state.handle_request()
            self.state.transition_to_next_state()

if __name__ == "__main__":
      traffic_light = TrafficLight(GreenState())
      traffic_light.request_next()
      traffic_light.request_next()
      traffic_light.request_next()
      traffic_light.request_next()

"""

Intent:
      - One-to-Many notification of an object to its notifiers 

Components:
      - Subject/Publisher => contains a reference to all the observers. Contains methods for attach, deattach and notify
      - Observer/Subscriber => has notify method to act when notiactions if erceives 


Use-case:
      - Tempareature from a weather station being updated on a phone display and TV display 
"""

from abc import abstractmethod, ABC
from typing import Any, List

class Publisher(ABC): # Also known as subject
      @abstractmethod
      def attach_observer(self, observer: Any):
            pass
      @abstractmethod
      def deattach_observer(self, observer: Any):
            pass
      @abstractmethod
      def notify_observers(self):
            pass

class Subscriber(ABC): # Also know as observer
      @abstractmethod
      def update(self, temparature, humidity):
            pass

class WeatherStation(ABC):
      def __init__(self) -> None:
            self._list_of_observers: List[Subscriber] = []
            self._temperature = None
            self._humidity = None
      def attach_observer(self, observer: Any):
            self._list_of_observers.append(observer)
      def deattach_observer(self, observer: Any):
            self._list_of_observers.remove(observer)
      def notify_observers(self):
            for observer in self._list_of_observers:
                  observer.update(self._temperature, self._humidity)
      def set_weather(self, temperature:int, humidity:int):
            self._temperature = temperature
            self._humidity = humidity
            self.notify_observers()
      
class PhoneDisplay(Subscriber):
      def update(self, temperature:int, humidity:int ):
            print(f"Phone being updated with temp: {temperature} and humidity: {humidity}")
class TVDisplay(Subscriber):
      def update(self, temperature:int, humidity:int ):
            print(f"TV being updated with temp: {temperature} and humidity: {humidity}")

if __name__ == "__main__":
      weather_station = WeatherStation()
      phone_subscriber = PhoneDisplay()
      TV_subscriber = TVDisplay()
      weather_station.attach_observer(phone_subscriber)
      weather_station.attach_observer(TV_subscriber)

      weather_station.set_weather(100, 80)
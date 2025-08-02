"""
Intent: controll access to object either for (cache) optimization or security 

Components:
      - Subject => common interface between real subject and proxy object
      - Proxy object => contains reference to actual objects
      - Real subject => actual object

Use case:
      - Blocking access to the object based on a given condition (for this toy example its randomly selected). We could use do caching when accessing an object. We showed a way to do so in flywieght
"""

from abc import ABC, abstractmethod
import random


class SecureDB(ABC):
      @abstractmethod
      def fetch_data(self):
            pass

class Database(SecureDB):
      def __init__(self, host, url, port) -> None:
            self._host = host
            self._url = url
            self._port = port
      def fetch_data(self):
            print(f"Fetching some very sensitive data!!!")

class ProxyDB(SecureDB):
      def __init__(self, host, url, port) -> None:
            self._db = Database(host, url, port)
      def fetch_data(self):
            allow_access = random.random() >= .5
            if allow_access:
                  self._db.fetch_data()
            else:
                  print("You dont have permission to acccess this")

if __name__ == "__main__":
      db = ProxyDB("127.0.0.1", "example.com", "3306")
      db.fetch_data()
      db.fetch_data()
      db.fetch_data()
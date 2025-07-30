

"""
Intent: make sure that there is only  single instance of a given class

Components:
      - Actual object

Flow:
      - When a class is instantiated (__new__ dunder/magic method) read access is request to a Lock. It is checked if a given instance of the class exists
      (via checking a class attr --not instance dependent attr). If existing, return instance, else 

Usecase:
      - Some logger

Note: a thread-safety alternative (much simpler) is to simple do a modular import of a single instance. In this case, however, u sacrifice the possibility to subclass the given 
class.

"""
import threading

class MyLogger:
      _instance = None
      _lock = threading.Lock()

      def __new__(cls):
            if not cls._instance:
                  with cls._lock:
                        cls._instance = super().__new__(cls)
            return cls._instance
      
      def __init__(self) -> None:
            if not hasattr(self, "_initialized"):
                  print("Logger: Initializing instance attributes (only once).")
                  self.log_file = "app.log"
                  self._initialized = True
            else:
                  print("Logger: __init__ called again, but attributes already initialized.")

      def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"{message}\n")
        print(f"Logged: {message}")

if __name__ == "__main__":
     instance_1 = MyLogger()
     instance_2 = MyLogger()

     instance_1_addr = id(instance_1) 
     instance_2_addr = id(instance_2) 
     print(f"Instance 1 memory addr: {instance_1_addr}")
     print(f"Instance 2 memory addr: {instance_2_addr}")

     if instance_1_addr != instance_2_addr:
            raise Exception("Singleton not properly implemented!")

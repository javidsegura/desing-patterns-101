"""

Intent: 
      - plug in some sadded funcionality/responsibility to an object without having to change the actual objects internal code

Note:
      - We are leveraging @wrapper functionality from python

"""

import logging 
import functools

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def logger_decorator(message):
      logger.debug("Im at the root level")
      def decorator(func):
            logger.debug(f"Message is: {message}")
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                  logger.debug(f"Executing: {func.__name__}, withs *args: {args}, **kwargs {kwargs}")
                  result = func(*args, **kwargs)
                  return result
            return wrapper
      return decorator

@logger_decorator(message="Hello world!")
def add_two_numbs(a,b):
      print(f"Adding two numbs: {a} and b: {b}")
      return a+b

if __name__ == "__main__":
      add_two_numbs(1,2)
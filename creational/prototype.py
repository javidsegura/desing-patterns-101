
"""
Intent: create a copy of an existing copy without having to re-instantiate with the same params (in some cases this may be too computationally expensive)

Components:
      - Actual Object 
Flow:
      - An existing object is passed to a cloner. The cloner receives an argument determining if the copy should be deep (recursive for internal objects) or not (keep a reference to
      nested objects)

Usecase:
      - Create mock db data object (heavy time to instantiate / private methods that obfuscate replication process)

Note: this design pattern is also called 'clone' alongside 'prototype'. 
"""

import copy

class Database():
      def __init__(self) -> None:
            self.some_very_computationally_expensive_data = None
      def fetch(self):
            self.some_very_computationally_expensive_data = "...."
      def copy(self, deep: bool = False):
            if deep:
                  return copy.deepcopy(self)
            else:
                  return copy.copy(self)
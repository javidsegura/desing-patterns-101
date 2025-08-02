"""

Intent: adjust modern API interfaces to old existing ones, keeping same functionality through a centralized/unified interface.

Components:
      - Target: the interface to adapt as a reference
      - Adaptee: the interface that need to adapt to Target
      - Adapter: middleman. Routes accordingly

Flow:
      - Clinet provides to adapter the Adaptee. Client calls a target method that gets routed to the corresponding in adaptee

Usecase:
      - Player receives a weapon, then call .fire on it. One such weapon is legacy and does not have .fire (and u cant change name cause its part of a 3rd party library)
"""

from abc import ABC, abstractmethod

class NewWeapon(ABC):
      @abstractmethod
      def fire(self):
            pass
class OldWeapon(ABC):
      @abstractmethod
      def shoot(self):
            pass

class Bazooka(NewWeapon): 
      def fire(self):
            return "Bazoooooooka"
class Laser(OldWeapon): # Adaptee (emulating legacy components)
      def shoot(self):
            return "ZZZZZ shoooooot"

class OldToNewWeaponAdapter(NewWeapon): # Adapter
      def __init__(self, old_weapon: OldWeapon) -> None:
            self._old_weapon = old_weapon
      def fire(self):
            return self._old_weapon.shoot()

if __name__ == "__main__":
      weapons = []

      weapons.append(Bazooka())
      old_weapon_adapted = OldToNewWeaponAdapter(Laser())
      weapons.append(old_weapon_adapted)

      for weapon in weapons:
            print(weapon.fire())
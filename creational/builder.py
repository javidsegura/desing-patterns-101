"""

Intent:
      - Highly customizable (with optional params) constructor can be broken down into sequence of steps. Then call those steps in a given order for different version

Components:
      - Object => Final object
      - Abstract Builder => defines all the steps to be executede (construction process) + final object
      - Concrete Builder 
      - Director (optional, client can do as well) => predefines a set of step for a given product variation

Use-case scenario:
      - A computer object is created. Variations in the builder are the specs of the computer. Variations in the director determine the number  of components included

"""

from abc import ABC, abstractmethod

class Computer():
      def __init__(self) -> None:
          self.cpu = None
          self.ram = None
          self.storage = None
          self.keyboard = None
          self.mouse = None
          self.gui = None
          self.microphone = None
          self.gpu = None 

      def __str__(self):
           return (f"Computer config:\n"
                   f"  CPU: {self.cpu}\n"
                   f"  RAM: {self.ram}\n"
                   f"  Storage: {self.storage}\n"
                   f"  GPU: {self.gpu}\n"
                   f"  Keyboard: {self.keyboard}\n"
                   f"  Mouse: {self.mouse}\n"
                   f"  GUI: {self.gui}\n"
                   f"  Microphone: {self.microphone}")


# -- Abstract builder --
class Builder(ABC):
      def __init__(self) -> None:
           self.computer = Computer()

      @abstractmethod
      def add_cpu(self, cpu_type: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_RAM(self, ram_size: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_storage(self, storage_type: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_keyboard(self, keyboard: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_mouse(self, mouse: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_gui(self, gui_type: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_microphone(self, mic_type: str = None) -> 'Builder':
            ...
      @abstractmethod
      def add_gpu(self, gpu_type: str = None) -> 'Builder': 
            ...

      def get_computer(self) -> Computer:
           return self.computer

# -- Concrete builder --
class GamingPCBuilder(Builder):
    def add_cpu(self, cpu_type: str = "Intel i9") -> 'GamingPCBuilder':
        self.computer.cpu = cpu_type
        return self

    def add_RAM(self, ram_size: str = "32GB DDR5") -> 'GamingPCBuilder':
        self.computer.ram = ram_size
        return self

    def add_storage(self, storage_type: str = "2TB NVMe SSD") -> 'GamingPCBuilder':
        self.computer.storage = storage_type
        return self

    def add_keyboard(self, keyboard: str = "Razer BlackWidow") -> 'GamingPCBuilder':
        self.computer.keyboard = keyboard
        return self

    def add_mouse(self, mouse: str = "Logitech G502 Hero") -> 'GamingPCBuilder':
        self.computer.mouse = mouse
        return self

    def add_gui(self, gui_type: str = "4K 144Hz Monitor") -> 'GamingPCBuilder':
        self.computer.gui = gui_type
        return self

    def add_microphone(self, mic_type: str = "Blue Yeti X") -> 'GamingPCBuilder':
        self.computer.microphone = mic_type
        return self

    def add_gpu(self, gpu_type: str = "NVIDIA GeForce RTX 4090") -> 'GamingPCBuilder': 
        self.computer.gpu = gpu_type
        return self


class OfficePCBuilder(Builder):
    def add_cpu(self, cpu_type: str = "Intel i5") -> 'OfficePCBuilder':
        self.computer.cpu = cpu_type
        return self

    def add_RAM(self, ram_size: str = "8GB DDR4") -> 'OfficePCBuilder':
        self.computer.ram = ram_size
        return self

    def add_storage(self, storage_type: str = "256GB SSD") -> 'OfficePCBuilder':
        self.computer.storage = storage_type
        return self

    def add_keyboard(self, keyboard: str = "Dell Basic Keyboard") -> 'OfficePCBuilder':
        self.computer.keyboard = keyboard
        return self

    def add_mouse(self, mouse: str = "Microsoft Optical Mouse") -> 'OfficePCBuilder':
        self.computer.mouse = mouse
        return self

    def add_gui(self, gui_type: str = "1080p Standard Monitor") -> 'OfficePCBuilder':
        self.computer.gui = gui_type
        return self

    def add_microphone(self, mic_type: str = "Integrated Laptop Mic") -> 'OfficePCBuilder':
        self.computer.microphone = mic_type
        return self

    def add_gpu(self, gpu_type: str = "Integrated Intel UHD Graphics") -> 'OfficePCBuilder': 
        self.computer.gpu = gpu_type
        return self
 
#  -- DIRECTOR -- 
class Director():
      def __init__(self) -> None:
            self._builder = None
      
      def set_builder(self, builder: Builder):
           self._builder = builder

      def create_simple_pc(self):
            return self._builder.add_cpu().add_RAM().add_storage().add_keyboard().add_mouse().add_gui()

      def create_complete_pc(self):
            return self._builder.add_cpu().add_RAM().add_storage().add_keyboard().add_mouse().add_gui().add_microphone().add_gpu()
      
if __name__ == "__main__":
     office_builder = OfficePCBuilder()
     director = Director()
     director.set_builder(office_builder)
     director.create_simple_pc()
     print(office_builder.computer)

     print("="*30)

     gaming_builder = GamingPCBuilder()
     director.set_builder(gaming_builder) # recycling existing object!
     director.create_complete_pc()
     print(gaming_builder.computer)
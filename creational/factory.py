
"""
Intent: decoupling the what and the how from an object creational process

Components:
      - Abstract factory => executes concrete product methods + contains abstract method
      - Concrete factory => returns the concrete object
      - Abstract product => set of universal methods for all objects to contain
      - Concrete product => actual object being created 
Flow:
      - Client instantiates ConcreteFactory. Calls method inherited from abstract factory that modify concrete object

Use-case scenario:
      - Opening and writing to files. Files type: PDF, PowerPoint, Excel

"""

from abc import abstractmethod, ABC

class Document(ABC): # Abstract product  
      @abstractmethod
      def open(self):
            pass

      @abstractmethod
      def write(self):
            pass
class PDFDocument(Document):
      def __init__(self, filename: str) -> None:
            self.filename = filename
            
      def open(self):
            print(f"Opening PDF: {self.filename}")

      def write(self):
            print(f"Writing to PDF: {self.filename}")

class PowerPointDocument(Document):
      def __init__(self, filename: str) -> None:
            self.filename = filename
            
      def open(self):
            print(f"Opening PowerPoint: {self.filename}")

      def write(self):
            print(f"Writing to PowerPoint: {self.filename}")

class ExcelDocument(Document):
      def __init__(self, filename: str) -> None:
            self.filename = filename
            
      def open(self):
            print(f"Opening Excel: {self.filename}")

      def write(self):
            print(f"Writing to Excel: {self.filename}")

class Creator(ABC):
      @abstractmethod
      def factory_method(self, filename: str) -> Document:
            pass

      def create_and_open_document(self, filename: str):
            document = self.factory_method(filename=filename)
            document.open()
            return document

class PDFCreator(Creator):
      def factory_method(self, filename: str) -> Document:
            return PDFDocument(filename)
class PowerPointCreator(Creator):
      def factory_method(self, filename: str) -> Document:
            return PowerPointDocument(filename)
class ExcelCreator(Creator):
      def factory_method(self, filename: str) -> Document:
            return ExcelDocument(filename)
      
if __name__ == "__main__":
      print(f"------ PDF ------")
      PDFCreator().create_and_open_document("report.pdf")
      print(f"------ PowerPoint ------")
      PowerPointCreator().create_and_open_document("report.ppt")
      print(f"------ Excel ------")
      ExcelCreator().create_and_open_document("report.xls")
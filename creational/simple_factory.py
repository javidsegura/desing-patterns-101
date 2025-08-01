"""
Intent: factory that call the Creator based on passed paramter  
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
            g(f"Opening PDF: {self.filename}")

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

class Creator(ABC): # Factories 
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
      
class SimpleFactory():
      def __init__(self, object_type: str) -> None:
            if object_type == "pdf":
                  self.object = PDFCreator()
            elif object_type == "ppt":
                  self.object = PowerPointCreator()
            else:
                  self.object = ExcelCreator()
      
if __name__ == "__main__":
      SimpleFactory("pdf")
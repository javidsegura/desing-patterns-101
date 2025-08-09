"""
Intent: allowing several iteration methods with the same interface 

Components: 
      - Iterator (interface) => interface for iterating (e.g., hasNext(), next() -- may be language specific, such as in Python)
      - Concrete iterator
      - Aggeragator => bings the interation method 

Flow:
      - Client binds to the aggregator the given iteration method.
      - Factory used for __iter__ method
      - Returned object has to have __next__ and raise StopIteration at some moment

Usecase:
      - Several binary trees methods
"""

from abc import ABC, abstractmethod
from typing import List

class Node():
      def __init__(self, val) -> None:
            self.data = val
            self.left = None
            self.right = None

class Iterator(ABC):
      @abstractmethod
      def __next__(self):
            pass

class InOrder(Iterator):
      def __init__(self, root: Node) -> None:
           self._stack: List[Node] = []
           self._push_left(root)
      def __next__(self):
            if not self._stack:
                  raise StopIteration
            node = self._stack.pop()
            self._push_left(node.right)
            return node.data

      def _push_left(self, node: Node):
            while node:
                  self._stack.append(node)
                  node = node.left

class PreOrder(Iterator):
      def __init__(self, root: Node) -> None:
            self._stack: List[Node] = [root]
      def __next__(self):
            if not self._stack:
                  raise StopIteration
            node = self._stack.pop()
            if node.right:
                  self._stack.append(node.right)
            if node.left:
                  self._stack.append(node.left)
            return node.data

class PostOrder(Iterator):
      def __init__(self, root: Node) -> None:
            self._stack: List[Node] = []
            self._processingList: List[Node] = []
            self.add_children(root)
      def __next__(self):
            if not self._stack:
                  raise StopIteration
            node = self._stack.pop()
            return node.data
      
      def add_children(self, root: Node):
            self._processingList.append(root)
            while self._processingList:
                  node = self._processingList.pop()
                  self._stack.append(node)
                  if node.left:
                        self._processingList.append(node.left)
                  if node.right:
                        self._processingList.append(node.right)


class BinaryTree():
      def __init__(self, root: Node, iteration_method: str) -> None:
            self.root = root
            self.iteration_method = iteration_method

      def __iter__(self):
            match self.iteration_method:
                  case "pre":
                        return PreOrder(root=self.root)
                  case "in":
                        return InOrder(root=self.root)
                  case "post":
                        return PostOrder(root=self.root)

if __name__ == "__main__":
      tree_data = BinaryTree(Node(10), iteration_method="pre")
      tree_data.root.left = Node(2)
      tree_data.root.right = Node(6)
      tree_data.root.left.left = Node(1)
      tree_data.root.left.right = Node(3)
      tree_data.root.right.left = Node(5)
      tree_data.root.right.right = Node(7)

      # 1: Pre
      for node in tree_data:
            print(node)
      print("="*40)
      # 2: In
      tree_data.iteration_method = "in"
      for node in tree_data:
            print(node)
      print("="*40)
      # 3: Post
      tree_data.iteration_method = "post"
      for node in tree_data:
            print(node)
      print("="*40)


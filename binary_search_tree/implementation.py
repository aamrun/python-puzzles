#Implementation of python-puzzles/binary_search_tree

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def insert_node(self,value):
    if self is not None and self.value < value and self.right is None:
     self.right = Node(value)
    elif self is not None and self.value >= value and self.left is None:
     self.left = Node(value)
    elif self is not None and self.value < value:
     self.right.insert_node(value)
    elif self is not None and self.value >= value:
     self.left.insert_node(value)

  def build_tree(self,value_list):
    for value in value_list:
      self.insert_node(value)

  def inorder_traversal(self):
    if self:
     if self.left:
      self.left.inorder_traversal()
     print(self.value)
     if self.right:
      self.right.inorder_traversal()

  def preorder_traversal(self):
    if self:
     print(self.value)
     if self.left:
      self.left.preorder_traversal()
     if self.right:
      self.right.preorder_traversal()

  def postorder_traversal(self):
    if self:
     if self.left:
      self.left.postorder_traversal()
     if self.right:
      self.right.postorder_traversal()
     print(self.value)

new_root = Node(9)
new_root.build_tree([5,3,7,2,5,2,7,3,7,2,9])
print("Inorder Traversal")
new_root.inorder_traversal()
print("Preorder Traversal")
new_root.preorder_traversal()
print("Postorder Traversal")
new_root.postorder_traversal()

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

  def invert(self):
    temp = self.left
    self.left = self.right
    self.right = temp

    if self.left:
     self.left.invert()
    if self.right:
     self.right.invert()

new_root = Node(9)
new_root.build_tree([5,3,7,2,5,2,7,3,7,2,9])
print("\nInorder Traversal\n")
new_root.inorder_traversal()
print("\nPreorder Traversal\n")
new_root.preorder_traversal()
print("\nPostorder Traversal\n")
new_root.postorder_traversal()

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

print("\nBefore Inversion\n")
root.preorder_traversal()
# a b d e c f 
print("\nAfter Inversion\n")
root.invert()
root.preorder_traversal()
# a c f b e d

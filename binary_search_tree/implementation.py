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
     print(self.value, end = " ")
     if self.right:
      self.right.inorder_traversal()

  def preorder_traversal(self):
    if self:
     print(self.value, end = " ")
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
     print(self.value, end = " ")

  def invert(self):
    temp = self.left
    self.left = self.right
    self.right = temp

    if self.left:
     self.left.invert()
    if self.right:
     self.right.invert()

  def findFloorCeiling(self, value, floor=None, ceil=None):
    tree_stack,found_floor,found_ceil = [self],None,None

    while len(tree_stack)!=0:
     node = tree_stack.pop()
     if node.value == floor or node.value == value - 1:
      found_floor = node.value
     elif node.value == ceil or node.value == value + 1:
      found_ceil = node.value
     
     if node.left:
      tree_stack.append(node.left)
     if node.right:
      tree_stack.append(node.right)

    return found_floor,found_ceil

  def tree_depth(self):
    if self:
     return max(1 + self.left.tree_depth() if self.left else 0, 1 + self.right.tree_depth() if self.right else 0)
    return 0

  def deepest(self):
    first_stack,second_stack,depth,node_value = [self],[],0,None

    while first_stack!=[] or second_stack!=[]:
     if first_stack!=[]:
      depth += 1
      node_value = first_stack[0].value
      while first_stack!=[]:
       node = first_stack.pop()
       if node.left:
        second_stack.append(node.left)
       if node.right:
        second_stack.append(node.right)

     if second_stack!=[]:
      depth += 1
      node_value = second_stack[0].value
      while second_stack!=[]:
       node = second_stack.pop()
       if node.left:
        first_stack.append(node.left)
       if node.right:
        first_stack.append(node.right)

    return node_value,depth

  def nodes_at_depth(self,target_depth):
    if target_depth == 0:
     return self.value if self else None

    first_stack,second_stack,depth,node_value = [self],[],0,None

    while first_stack!=[] or second_stack!=[]:
     if first_stack!=[]:
      depth += 1
      node_value = first_stack[0].value
      while first_stack!=[]:
       node = first_stack.pop()
       if node.left:
        second_stack.append(node.left)
       if node.right:
        second_stack.append(node.right)

      if depth == target_depth and second_stack!=[]:
       return [node.value for node in second_stack]

     if second_stack!=[]:
      depth += 1
      node_value = second_stack[0].value
      while second_stack!=[]:
       node = second_stack.pop()
       if node.left:
        first_stack.append(node.left)
       if node.right:
        first_stack.append(node.right)

     if depth == target_depth and first_stack!=[]:
      return [node.value for node in first_stack]

    return None

  def validate_bst(self):
    if self.left is None and self.right is None:
     return True
    elif self.left and self.right is None:
     return self.left.value < self.value and self.left.validate_bst()
    elif self.right and self.left is None:
     return self.right.value > self.value and self.right.validate_bst()
    else:
     return self.left.value < self.value and self.right.value > self.value and self.right.validate_bst() and self.left.validate_bst()

new_root = Node(9)
new_root.build_tree([5,3,7,2,5,2,7,3,7,2,9])
print("\nInorder Traversal\n")
new_root.inorder_traversal()
print("\nPreorder Traversal\n")
new_root.preorder_traversal()
print("\nPostorder Traversal\n")
new_root.postorder_traversal()

print(f"\nTree depth : {new_root.tree_depth()}")

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

print(f"\nTree depth : {root.tree_depth()}")

print("\nFloor and Ceiling of a binary tree.\n")

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(root.findFloorCeiling(5 , 4 , 6))

print(f"\nTree depth : {root.tree_depth()}")

root = Node('a')
root.left = Node('b')
root.left.right = Node('e')
root.left.right.left = Node('f')
root.left.left = Node('d')
root.right = Node('c')

print(f"\nDeepest node : {root.deepest()}")

a = Node(5)
a.left = Node(3)
a.right = Node(7)
a.left.left = Node(1)
a.left.right = Node(4)
a.right.left = Node(6)
print(f"Work in Progess : Validate BST : {a.validate_bst()}")

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(f"Nodes at depth 2 : {a.nodes_at_depth(2)}")
# [4, 5, 7]

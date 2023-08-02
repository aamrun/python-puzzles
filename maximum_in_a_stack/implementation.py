#Added implementation for python-puzzles/maximum_in_a_stack

#This is simply a thin wrapper on a Python list and is in stark contrast to linked lists and trees which are implemeted in Python in the same way as C.

class MaxStack:
  def __init__(self):
    self.stack = []

  def push(self, val):
    self.stack.insert(0,val)

  def pop(self):
    if self.stack != []:
     self.stack.pop(0)

  def max(self):
    if self.stack == []:
     return None
    else:
     return max(self.stack)

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2

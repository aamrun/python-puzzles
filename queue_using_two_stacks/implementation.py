#Implementation of python-puzzles/queue_using_two_stacks

#Similar to maximum_in_a_stack/implementation.py, this is a very straight forward implementation using Python lists.

class Queue:
  def __init__(self):
    self.input_stack = []
    self.output_stack = []
    
  def enqueue(self, val):
    self.input_stack.insert(0,val)

  def dequeue(self):
    if self.output_stack == []:
     self.output_stack = self.input_stack
     self.input_stack = []
    return self.output_stack.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3

#Implementation of python-puzzles/intersection_of_linked_lists

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None

  def intersection(self,second_list):
    self_token = self

    while self_token:
     second_token = second_list

     while second_token:
      if self_token.val == second_token.val:
       return self_token
      second_token = second_token.next

     self_token = self_token.next

    return None

  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = a.intersection(b)
c.prettyPrint()
#3 4

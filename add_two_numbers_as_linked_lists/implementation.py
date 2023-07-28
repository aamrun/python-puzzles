#Implementation of python-puzzles/add_two_numbers_as_linked_lists

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    holder = c
    if l1 is not None:
     holder += l1.val
    if l2 is not None:
     holder += l2.val

    if holder <= 9:
     c = 0
    else:
     c = 1

    l3 = ListNode(holder%10)
    if l1.next is None and l2.next is not None:
     l3.next = self.addTwoNumbers(None, l2.next,c)
    elif l1.next is not None and l2.next is None:
     l3.next = self.addTwoNumbers(l1.next,None,c)
    elif l1.next is not None and l2.next is not None:
     l3.next = self.addTwoNumbers(l1.next,l2.next,c)
    elif l1.next is None and l2.next is None and c == 1:
     l3.next = ListNode(c)
    
    return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8

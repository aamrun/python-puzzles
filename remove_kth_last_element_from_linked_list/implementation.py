#Implementation of python-puzzles/remove_kth_last_element_from_linked_list

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
  list_length = len(head.__str__().split(", "))
  
  if k == list_length:
   return head.next

  token = head

  current_position = list_length

  while current_position > k+1:
   token = token.next
   current_position-=1

  #Removes node from memory

  decoy = token.next
  token.next = decoy.next
  decoy = None

  #Does not remove node from memory
  #token.next = token.next.next

  return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]


# create a node first 
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
        
# create a linked list
class LinkedList:
   def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 0
    
# LL Reverse Between
# Qn. write a method to reverse a linked list from node m to node n inclusive.
# If the linked list is empty, then return None. 
    
   def reverse_between(self, m, n):
      # if the linked list is empty, then return None.
      if not self.head:
         return None 
      # create a dummy node and connect it to the head.
      dummy = Node(0)
      dummy.next = self.head
      prev = dummy
      # move prev to the node at position m.
      for _ in range(m):
         prev = prev.next  
      # set current to the next node of prev.
      current = prev.next
      
      # Reversing the linked list from position m to n.
      for _ in range(n - m):
         temp = current.next
         current.next = temp.next
         temp.next = prev.next 
         prev.next = temp
         
      # update the head of the linked list with the next node of the dummy.
      self.head = dummy.next
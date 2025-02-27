class Node:
   def __init__ (self, value):
      self.value = value
      self.next = None
   
class DoubleLinkedList:
   def __init__ (self, value):
      self.value = value
      self.head = None
      self.tail = None

   # Swap First and Last 
   # Qn. Swap the values of the first and last node

   def swap_first_last(self):
      # Check if the list is empty or has only one node
      if self.head is None or self.head == self.tail:
         return
      # Swap the values of the head and tail nodes using tuple assignment
      self.head.value, self.tail.value = self.tail.value, self.head.value
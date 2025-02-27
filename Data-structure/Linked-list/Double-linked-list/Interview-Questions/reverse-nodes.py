class Node:
   def __init__ (self, value):
      self.value = value
      self.next = None
   
class DoubleLinkedList:
   def __init__ (self, value):
      self.value = value
      self.head = None
      self.tail = None

   # Reverse
   # Qn. Reversing the order of the nodes in the list, i.e., first node becomes
   # the last node, the second node becomes the second-to-last node, and so on.

   def reverse(self):
      # creating a variable temp and setting it to the head of the list
      # it use for traverse the list and perform the swap operation on each node
      temp = self.head
      # traversing 
      while temp is not None:
         # swap the prev and next pointer using tuple packing and unpacking syntax
         temp.prev, temp.next = temp.next, temp.prev
         
         # move to the next node
         temp = temp.prev
         
      # swap the head and tail pointers
      self.head, self.tail = self.tail, self.head
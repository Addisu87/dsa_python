class Node:
   def __init__ (self, value):
      self.value = value
      self.next = None
   
class DoubleLinkedList:
   def __init__ (self, value):
      self.value = value
      self.head = None
      self.tail = None

      # Palindrome Checker
      # Qn. Write a method to determine whether a given doubly linked list 
      # reads the same forwards and backwards.
   
   def is_palindrome(self):
      # If the length of the list is 0 or 1, it's always palindrome
      if self.length <= 1:
         return True
      
      # Create two pointers, one starting from the head and the other from the tail
      forward_node = self.head
      backward_node = self.tail
      
      # Iterate over half of the list
      for _ in range(self.length // 2):
         # If the values at the two ends of the list do not match,
         # the list is not palindrome
         if forward_node.value != backward_node.value:
            return False
         
         # Move the two pointer towards each other
         forward_node = forward_node.next
         backward_node = backward_node.prev
         
      # If all values matched, the list is a palindrome 
      return True 
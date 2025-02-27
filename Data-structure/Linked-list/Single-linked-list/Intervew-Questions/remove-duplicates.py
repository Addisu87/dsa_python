
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
                
    
# SLL Remove Duplicates in SLL
# Qn. Implement a method to remove duplicates in SLL
# Example: 
# Input:
    #LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
# Output:
    # LinkedList: 1 -> 2 -> 3 -> 4 -> 5
    
    # solution-1 using a Set method to have time complexity of O(n):
    
   def remove_duplicates(self):
      # declare an empty set as values
      values = set()
      # Initialize two pointers to show the starting point of the list
      previous = None
      current = self.head 
      # iterated over
      while current:
         # if it's is duplicate, remove it from a SLL
         if current.value in values:
               previous.next = current.next
               self.length -= 1
         else:
               # add to the set
               values.add(current.value)
               previous = current 
      # iteration continues until current is None:    
      current = current.next
        
    # solution-2 without using a Set method,
    # we will have time complexity of O(n^2):
    
   def remove_duplicates(self):
      current = self.head
      while current: 
         runner = current
         while runner.next:
               if runner.next.value == current.value:
                  runner.next = runner.next.next
                  self.length -= 1
               else: 
                  runner = runner.next
         current = current.next
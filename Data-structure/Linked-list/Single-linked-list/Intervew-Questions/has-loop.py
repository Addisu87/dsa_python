
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

# SLL has Loop
# Qn. Write a method that should utilize Floyd's cycle-finding algorithm(tortoise and hare algorithm)
# to determine there is a cycle or loop efficiency and it present in the SLL 
            
   def has_loop(self):
      # pointers to traverse a SLL:
      slow = self.head
      fast = self.head
      
      while fast is not None and fast.next is not None:
         slow = slow.next   # Move slow pointer one step
         fast = fast.next.next   # Move fast pointer two steps
         
         # if there is a loop in the SLL,
         # the slow and fast pointer will eventually meet
         if slow == fast:
               return True
      
      # otherwise, there is no loop, it return False:
      return False
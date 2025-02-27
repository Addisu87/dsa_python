# Linked-list based queues

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
class Queue:
   def __init__(self):
      self.first = None
      self.last = None
      self.count = 0
      
   # enqueue operation
   def enqueue(self, data):
      new_node = Node(data)
      
      if self.first is None:
         self.first = new_node
         self.last = self.first
      else:
         new_node.prev = self.last
         self.last.next = new_node
         self.last = new_node
         
      self.count += 1
      
      
   # dequeue operation
   def dequeue(self):
      if self.count < 1:
         print("Queue is empty")
      
      elif self.count == 1:
         self.first = None
         self.last = None
         self.count -= 1
         
      else:
         self.first = self.first.next
         self.first.prev = None
         
      self.count -= 1
         
   
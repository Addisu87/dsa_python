# class for Node with data and priority
class Node:
   def __init__(self, info, priority):
      self.info = info
      self.priority = priority
      
# class for Priority queue
class PriorityQueue:
   def __init__(self):
      self.queue = []
      
   def show(self):
      for x in self.queue:
         print(str(x.info)+ " - "+ str(x.priority))
      
   # Insert method
   def insert(self, new_node):
      if len(self.queue) == 0:
         # add the new node
         self.queue.append(new_node)
      else:
         # traverse the queue to find the right place for new node
         for x in range(0, len(self.queue)):
            # if the priority of new node is greater
            if new_node.priority >= self.queue[x].priority:
            # if we have traversed the complete queue
               if x == (len(self.queue) - 1):
                  # add new node at the end
                  self.queue.insert(x + 1, new_node)
               else:
                  continue
            else:
               self.queue.insert(x, new_node)
               return True
         
   # Delete method
   def delete(self):
      # remove the first node from the queue
      x = self.queue.pop(0)
      print("Delete date with the given priority-", x.info, x.priority)
      return x
   
my_pryqueue = PriorityQueue()
my_pryqueue.insert(Node("Cat", 13))
my_pryqueue.insert(Node("Rat", 2))
my_pryqueue.insert(Node("Bat", 1))
my_pryqueue.insert(Node("Ant", 26))
my_pryqueue.insert(Node("Lion", 25))
my_pryqueue.show()
my_pryqueue.delete()
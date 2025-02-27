class PriorityQueueHeap:
   def __init__(self):
      # a list of tuples
      self.heap = [()]
      self.size = 0
      
   def arrange(self, k):
      while k // 2 > 0:
         if self.heap[k][0] < self.heap[k // 2][0]:
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
         k //= 2
         
   def insert (self, priority, item):
      self.heap.append((priority, item))
      self.size += 1
      self.arrange(self.size)
      
   def minChild(self, k):
      if k * 2 + 1 > self.size:
         return k * 2
      elif self.heap[k * 2][0] < self.heap[k * 2 + 1][0]:
         return k * 2
      else:
         return k * 2 + 1
      
   def sink(self, k):
      while k * 2 <= self.size:
         mc = self.minChild(k)
         if self.heap[k][0] > self.heap[mc][0]:
            self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
         k = mc
         
   def delete_at_root(self):
      item = self.heap[1][1]
      self.heap[1] = self.heap[self.size]
      self.size -= 1
      self.heap.pop()
      self.sink(1)
      return item
   
my_PQH = PriorityQueueHeap()

my_PQH.insert(2, "Bat")
my_PQH.insert(13, "Cat")
my_PQH.insert(18, "Rat")
my_PQH.insert(26, "Ant")
my_PQH.insert(3, "Lion")
my_PQH.insert(4, "Bear")
my_PQH.heap

for _ in range(my_PQH.size):
   n = my_PQH.delete_at_root()
   print(n)
   print(my_PQH.heap)
# the value of the parent node must always be
# less than or equal to its children
class MinHeap:
   def __init__(self):
      self.heap = [0]
      self.size = 0

   # Insert operation of heap 
   
   # create helper method, called arrange
   # This method ensures that the elements are ordered properly
   def arrange(self, k):
      # using integer division
      while k // 2 > 0:
         # compare the values between the parent and child node
         # If the parent is greater than the child, swap the two values
         if self.heap[k] < self.heap[k // 2]:
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
         # after each iteration, we move up in the tree
         k //= 2
         
      
   def insert(self, item):
      self.heap.append(item)
      self.size += 1
      # reorganize the heap (heapify it)
      self.arrange(self.size)
      
      
   # Delete operation of heap
   # a helper method for finding out which of the children
   #  to compare against the parent node
   def minChild(self, k):
      # beyond the end of the list—
      # return the index of the left child
      if k * 2 + 1 > self.size:
         return k * 2
      # Otherwise, return the index of the lesser of the two children
      elif self.heap[k * 2] < self.heap[k * 2 + 1]:
         return k * 2
      else: 
         return k * 2 + 1
   
   # percolate-down process
   def sink(self, k):
      # loop until the end of the tree 
      # so that we can sink (move down)
      while k * 2 <= self.size:
         # set the left or right children to compare against
         mc = self.minChild(k)
         # compare parent and child, to make the swap
         if self.heap[k] > self.heap[mc]:
            self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
         # make sure that we move down the tree
         k = mc
         
   # deletion of the root node
   def delete_at_root(self):
      # copy the root element in a variable item
      item = self.heap[1]
      # the last element is moved to the root node
      self.heap[1] = self.heap[self.size]
      # reduce the size of the heap
      self.size -= 1
      self.heap.pop()
      # reorganize the heap element
      self.sink(1)
      return item
   
   # Deleting an element at a specific location from a heap
   def delete_at_location(self, location):
      item = self.heap[location]
      self.heap[location] = self.heap[self.size]
      self.size -= 1
      self.heap.pop()
      self.sink(location)
      return item
   
   # Heap sort
   def heap_sort(self):
      sorted_list = []
      for _ in range(self.size):
         n = self.delete_at_root()
         sorted_list.append(n)
         
      return sorted_list
   
      
my_heap = MinHeap()
# for i in (2, 3, 5, 7, 9, 10, 6):
#    my_heap.insert(i)
   
# print(my_heap.heap)

# print(my_heap.delete_at_root())
# print(my_heap.delete_at_location(2))
# print(my_heap.heap)
   
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsorted_list:
   my_heap.insert(i)
   
print("Unsorted list: {}".format(unsorted_list))

print("Sorted list: {}".format(my_heap.heap_sort()))

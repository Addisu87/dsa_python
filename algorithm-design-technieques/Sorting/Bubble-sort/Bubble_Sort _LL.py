# Bubble Sort of LL (⚡Interview Question)

# Write a bubble_sort() method in the LinkedList class that will sort the elements
# of a linked list in ascending order using the bubble sort algorithm.

def bubble_sort(self):
   if self.length < 2:
      return 
   
   sorted_until = None
   
   while sorted_until != self.head.next:
      current = self.head
      while current.next != sorted_until:
         next_node = current.next
         if current.value > next_node.value:
            current.value, next_node.value = next_node.value, current.value
            
         current = current.next
   sorted_until = current
   
   self.tail = current
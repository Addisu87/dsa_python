class Node:
   def __init__ (self, value):
      self.value = value
      self.next = None
   
class DoubleLinkedList:
   def __init__ (self, value):
      self.value = value
      self.head = None
      self.tail = None

   # Swap Nodes in Pairs(Double Linked List)
   # Qn. Swaps the values of the adjacent nodes in the DLL.
   # The method should not take any input parameters
   # DLL have not a tail
   
   def swap_pairs(self):
      # Create a dummy node as a placeholder
      dummy = Node(0)
      # Connect dummy node to head
      dummy.next = self.head
      # Set prev as a dummy node
      prev = dummy
      
      # Iterate through the list while a pair exists
      while self.head and self.head.next:
         # Assign first and second nodes of the pair
         first_node = self.head
         second_node = self.head.next
         
         # Swap the pair by updating pointers
         prev.next = second_node
         first_node.next = second_node.next
         second_node.next = first_node
         
         # Update prev pointes for swapped nodes
         second_node.prev = prev
         first_node.prev = second_node
         
         # Update prev pointers of the next node
         if first_node.next:
            first_node.next.prev = first_node
            
         # Move head to the next pair
         self.head = first_node.next 
         # Update prev to the last node in pair
         prev = first_node
         
      # Update the head to the new start
      self.head = dummy.next
      
   


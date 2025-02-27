
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

# Find Kth Node From End
# Qn. Find the item that is a certain number of steps away from the end of the SLL,
# Without using length. ll=linked list and k=index
    
   def find_kth_from_end(ll, k):
      # Initialize both slow and fast pointers to 
      # the head node of the linked list
      slow = fast = ll.head
      # Move the fast pointer k nodes ahead of the slow pointer
      for _ in range(k):
         if fast is None:
               return None
         fast = fast.next     
      # Move both pointer one node at a time until the fast pointer
      # reaches the end of the linked list (None).
      # The slow pointer will now be pointing at the kth value
      while fast:
         slow = slow.next
         fast = fast.next
      # Return the kth node from the end of the linked list
      return slow
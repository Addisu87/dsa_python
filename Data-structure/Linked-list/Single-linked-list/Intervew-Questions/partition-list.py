
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
        
# LL partition List
# Qn. implementing a method partition_list(self, x) that will take an integer x and 
# partition the linked list such that all nodes with values less than x 
# come before nodes with values greater than or equal to x.
# It is given with out tail.

# This function partitions a SLL based on a given value x
    
    def partition_list(self, x):
        # if LL is empty, return None
        if not self.head:
            return None
        # Create two dummy nodes to be used as placeholders
        # One will hold values < x and other will hold values <= x
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        # Start with the head node of the LL
        current = self.head
        # Traverse through the LL and move each node to either
        # dummy1 or dummy2 depends on its value compared to x
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        # terminate dummy2 list with None
        prev2.next = None
        # Combine the two partitioned LL by pointing the last node
        # in the dummy1 list to the first node in the dummy2 list
        prev1.next = dummy2.next
        # Set the head of the LL to the first node is dummy1
        self.head = dummy1.next
        
        
        
        
        

        
        



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

    # Find middle node in SLL
    # Qn. write a method to find and return the middle node in the Linked List
    # without using the length attribute

    def find_middle_node(self):
        # Initialize two pointers to the head of the list
        slow = self.head
        fast = self.head

        # Traverse the list with the fast pointer moving twice
        # as fast as the slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

        # When the fast pointer reaches the end,
        # the slow pointer will be at the middle node
        return slow

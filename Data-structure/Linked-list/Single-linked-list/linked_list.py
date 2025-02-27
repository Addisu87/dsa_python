class Node:
    # create new Node
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # constructor
    def __init__(self, value):
        # encapsulate the value in a Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # print list method, to show all list elements
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # add Node to end
        # create a new node with a given value
        new_node = Node(value)

        # check if the linked list is empty:
        if self.head is None:
            # Point both head and tail at the new_node:
            self.head = new_node
            self.tail = new_node
        else:
            # Point the next pointer of the last node at the new_node:
            self.tail.next = new_node
            # set tail to point to new_node:
            self.tail = new_node
        # increment the length of SLL by 1:
        self.length += 1
        return True

    def prepend(self, value):
        # add Node to beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop(self):
        # remove Node at end
        # if there is no any node
        if self.length == 0:
            return None
        # if there a couple of nodes
        temp = self.head
        prev = self.head

        while (temp.next):
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1
        # if we have only one node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        # remove the first node
        if self.length == 0:
            # if there is no any node
            return None
        # if there a couple of nodes
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # if we have only one node
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        # get node value using index:
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        # set a new value
        temp = self.get(index)
        # use get method for DRY code

        # if temp is not None
        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        # insert a new node in between nodes
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        # remove item at a particular index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # reverse linked list
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # helper variables
        after = temp.next
        before = None
        # looping to traverse all nodes
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Bubble Sort of LL (⚡Interview Question)
    # Write a bubble_sort() method in the LinkedList class that will sort the elements
    # of a linked list in ascending order using the bubble sort algorithm.
    def bubble_sort(self):
        # Check if the list has less than 2 elements
        if self.length < 2:
            return

        # Initialize the sorted_until pointer to None
        sorted_until = None
        # Continue sorting until sorted_until reaches the second node
        while sorted_until != self.head.next:
            # Initialize current pointer to head of the list
            current = self.head
            # Iterate through unsorted portion of the list until sorted_until
            while current.next != sorted_until:
                next_node = current.next

                # Swap current and next_node values if current is greater
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value

                # Move current pointer to next node
                current = current.next
            # Update sorted_until pointer to the last node processed
            sorted_until = current
        # Update tail pointer to last node processed (i.e. largest element)
        self.tail = current

    # Selection Sort of LL (⚡Interview Question)
    # Write a selection_sort() method in the LinkedList class that will sort the elements
    # of a linked list in ascending order using the selection sort algorithm.
    def selection_sort(self):
        # If the linked list has less than 2 elements, it is already sorted
        if self.length < 2:
            return

        # Start with the first node as the current node
        current = self.head
        # While there is at least one more node after the current node
        while current.next is not None:
            # Assume the current node has the smallest value so far
            smallest = current
            # Start with the next node as the inner current node
            inner_current = current.next

            # Find the node with the smallest value among the remaining nodes
            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            # If the node with the smallest value is not the current node,
            # swap their values
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value
            # Move to the next node
            current = current.next
         # Set the tail of the linked list to the last node processed
        self.tail = current

    # Insertion Sort of LL (⚡Interview Question)
    # Write an insertion_sort() method in the LinkedList class that will sort the elements
    # of a linked list in ascending order using the insertion sort algorithm.

    def insertion_sort(self):
        # Check if the length of the list is less than 2
        if self.length < 2:
            return
        # Set the pointer to the first element of the sorted list
        sorted_list_head = self.head
        # Set the pointer to the second element of the list
        unsorted_list_head = self.head.next
        # Remove the first element from the sorted list
        sorted_list_head.next = None
        # Iterate through the unsorted list
        while unsorted_list_head is not None:
            # Save the current element
            current = unsorted_list_head
            # Move the pointer to the next element in the unsorted list
            unsorted_list_head = unsorted_list_head.next
            # Insert the current element into the sorted list
            if current.value < sorted_list_head.value:
                # If the current element is smaller than the first element
                # in the sorted list, it becomes the new first element
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                # Otherwise, search for the appropriate position to insert the current element
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        # Update the head and tail of the list
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp

  # Merge Two Sorted LL (⚡Interview Question)
  # Method to merge a linked list with another linked list


def merge(self, other_list):
    # Get the head node of the other linked list
    other_head = other_list.head
    # Create a dummy node to hold the merged list
    dummy = Node(0)
    # Set the current node to the dummy node
    current = dummy

    # Loop while both lists still have nodes
    while self.head is not None and other_head is not None:
        # Compare the values of the first nodes in each list
        if self.head.value < other_head.value:
            # If the value in the first list is smaller,
            # add it to the current node and move to the next node in the first list
            current.next = self.head
            self.head = self.head.next
        else:
            # Otherwise, add the value from the second list
            # and move to the next node in the second list
            current.next = other_head
            other_head = other_head.next

        # Move the current node to the next position
        current = current.next

    # If the first list still has nodes left, add them to the current node
    if self.head is not None:
        current.next = self.head
    else:
        # If the second list still has nodes left, add them to the current node
        current.next = other_head
        # Update the tail of the merged list to be the tail of the second list
        self.tail = other_list.tail

    # Set the head of the merged list to the next node after the dummy node
    self.head = dummy.next

    # Update the length of the merged list
    self.length += other_list.length


# Test constructor
# my_linked_list = LinkedList(4)
# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length, "\n")
# my_linked_list = LinkedList(4)
# my_linked_list.append(6)
# my_linked_list.append(8)
# my_linked_list.append(9)
l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

# Test set_value method
# my_linked_list.set_value(1, 4)

# my_linked_list.insert(1, 5)

# remove method
# print(my_linked_list.remove(2), "\n")

# reverse method
# print(my_linked_list.reverse())

# my_linked_list.print_list()

# Test prepend method

# my_linked_list.prepend(1)

# Test pop method

# (2) Items = Returns 2 Node
# print(my_linked_list.pop())

# (1) Items = Returns 1 Node
# print(my_linked_list.pop())

# (0) Items = Returns 0 Node
# print(my_linked_list.pop())

# Test pop_first method

# (2) Items = Returns 2 Node
# print(my_linked_list.pop_first())

# (1) Items = Returns 1 Node
# print(my_linked_list.pop_first())

# (0) Items = Returns None
# print(my_linked_list.pop_first())

# Test get method
# print(my_linked_list.get(2))


# print("Linked List Before Sort:")
# my_linked_list.print_list()

# my_linked_list.bubble_sort()

# print("\nSorted Linked List:")
# my_linked_list.print_list()


# print("Linked List Before Sort:")
# my_linked_list.print_list()

# my_linked_list.selection_sort()

# print("\nSorted Linked List:")
# my_linked_list.print_list()


# print("Linked List Before Sort:")
# my_linked_list.print_list()

# my_linked_list.insertion_sort()

# print("\nSorted Linked List:")
# my_linked_list.print_list()

print("Linked List-1 Before merge:")
l1.print_list()

print("\nLinked List-2 Before merge:")
l2.print_list()

print("\nMerged Linked List:")
l1.merge(l2)

l1.print_list()

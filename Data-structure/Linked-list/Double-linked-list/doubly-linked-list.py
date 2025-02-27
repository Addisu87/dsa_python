# Create a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    # constructor
    def __init__ (self, value):
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
        # add node at the end
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        return True
    
    def pop(self):
        # Remove node at the end
        # if we don't have any node
        if self.length == 0:
            return None
        
        temp = self.tail
        # if we have only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
        return temp
    
    def prepend(self, value):
        # add node at the beginning
        new_node = Node(value)
        
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # remove the first node
        # if we don't have any node
        if self.length == 0:
            return None
        
        temp = self.head 
         # if we have only one node
        if self.length == 1:
             self.head = None
             self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        # get item at a particular index 
        # check index
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:  
            temp = self.head
            for _ in range(index):
                temp = temp.next  
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    
    def set_value(self, index, value):
        # set a value of a node at a particular index
        # iterate an index using get to make DRY
        temp = self.get(index) 
        # if temp is not None  
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        # add a new node at any place 
        if index < 0 or index > self.length:
            return False
        
        # insert at the beginning
        if index == 0:
            return self.prepend(value)
        
        # insert at the end
        if index > self.length:
            return self.append(value)
        
        # insert at the middle
        new_node = Node(value)
        # create two pointers
        before = self.get(index - 1)
        after = before.next
        # connect the new_node pointers
        new_node.prev = before
        new_node.next = after
        # attach the new_node
        before.next = new_node 
        after.prev = new_node 
        # increment the length
        self.length += 1 
        return True
    
    def remove(self, index):
        # remove a node at any index
        # if index out of range
        if index < 0 or index > self.length:
            return False

        # if the node is at the beginning
        if index == 0:
            return self.pop_first()
        
        # if the node is at the end
        if index == self.length - 1:
            return self.pop()
        
        # if the node is in the middle
        # assign a new pointer
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        # remove the pointers
        temp.next = None
        temp.prev = None
        
        self.length -= 1
        return temp.value
    

my_doubly_linked_list = DoublyLinkedList(3)

# print("Head:", my_doubly_linked_list.head.value)
# print("Tail:", my_doubly_linked_list.tail.value)
# print("Length:", my_doubly_linked_list.length, "\n")

print("Doubly Linked List:")
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)

# my_doubly_linked_list.prepend(5)

# my_doubly_linked_list.set_value(1, 8)
# my_doubly_linked_list.insert(2, 5)
print(my_doubly_linked_list.remove(1), "\n")

my_doubly_linked_list.print_list()

# (2) Items = Returns 2 Node
# print(my_doubly_linked_list.pop())
# (1) Items = Returns 1 Node
# print(my_doubly_linked_list.pop())
# (0) Items = Returns 0 Node
# print(my_doubly_linked_list.pop())

# (2) Items = Returns 2 Node
# print(my_doubly_linked_list.pop_first())
# (1) Items = Returns 1 Node
# print(my_doubly_linked_list.pop_first())
# (0) Items = Returns 0 Node
# print(my_doubly_linked_list.pop_first())


# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))


        
        
        
        
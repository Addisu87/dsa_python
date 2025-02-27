# creating a node and traversing
class Node: 
    def __init__ (self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev   
        
class DoublyLinkedList:
    # create a doubly linked list class
    def __init__ (self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # Adding items
    
    def append_at_start(self, data):
        # append an item at beginning to the list.
        new_node = Node(data, None, None)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        
    def append(self, data):
        # append an item at the end of the list.
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        self.count += 1
        
    def append_at_a_location(self, data):
        # inserting a node at an intermediate position in the list
        current = self.head
        prev = self.head
        new_node = Node(data, None, None)
        while current: 
            if current.data == data: 
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                current.prev = new_node 
                self.count += 1
                
            prev = current
            current = current.next 
            
        # Querying a list  
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
            
    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print("Data item is present in the list.")
                return
        print("Data item is not present in the list.")
        return
        
        
    # Deleting items
    def delete(self, data):
        # delete a node from the list.
        current = self.head
        node_deleted = False
        
        if current is None:
            # list is empty
            print("List is empty")
            node_deleted == False
        
        elif current.data == data:
            # Item to be deleted is found at starting of the list
            self.head.prev = None
            node_deleted = True
            self.head = current.next 
            
        elif self.tail.data == data:
            # Item to be deleted is found at the end of list
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
            
        else: 
            while current: 
                # search item to be deleted, and delete the node
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
            
            if node_deleted == False:
                # Item to be deleted is not found in the list
                print("Item not found")
                
        if node_deleted: 
            self.count -= 1
                    
                 


#  create a double link list 
words = DoublyLinkedList()  
# append a new node at the starting of the list
words.append('egg')
words.append('ham')
words.append('spam')

print("Items in doubly linked list before append:")
current = words.head
while current:
    print(current.data)
    current = current.next
words.append_at_start('book')

print("Items in doubly linked list after append:")
current = words.head
while current:
    print(current.data)
    current = current.next
    
print("Items in doubly linked list after append")

words = DoublyLinkedList()  
# append a new node at the starting of the list
words.append('egg')
words.append('ham')
words.append('spam')

words.append('book')
print("Items in doubly linked list after adding element at end:")
current = words.head
while current:
    print(current.data)
    current = current.next
    
 # inserting a node at an intermediate position in the list  
words = DoublyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

words.append_at_a_location("ham")

print("Doubly linked list after adding an element after word \"ham\" in the list.")

current = words.head
while current:
    print(current.data)
    current = current.next 
    
# querying element in the list 
words = DoublyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

words.contains("ham")
words.contains("ham2")
    
    
#Code to create for a doubly linked list
words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# delete an element from a list
words.delete('ham')
current = words.head
while current:
    print(current.data)
    current = current.next
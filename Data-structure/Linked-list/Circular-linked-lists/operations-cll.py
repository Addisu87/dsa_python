
# creating a node
class Node:
    def __init__ (self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Creating circular linked lists
class CircularList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
        
        # Appending items
    def append(self, data):
        # append an element at the end of the circular list
        # based on a singly linked list
        node = Node(data)
        if self.tail:
            # check the list is empty
            self.tail.next = node
            self.tail = node 
            node.next = self.head
        else:
            self.head = node 
            self.tail = node
            self.tail.next = self.tail
        self.size += 1
        
    # traverse all the elements
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
            
    
    # deleting an element in a circular list
    def delete(self, data):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            if current.data == data: 
                if current == self.head:
                    # item to be deleted is head node
                    self.head = current.next
                    self.tail.next = self.head
                    
                elif current == self.tail:
                    # item to be deleted is tail node
                    self.tail = prev
                    prev.next = self.head
                    
                else:
                    # item to be deleted is an intermediate node
                    prev.next = current.next
            
                self.size -= 1
                return 
            
            prev = current
            current = current.next
        
             
words = CircularList()
words.append("eggs")
words.append("ham")
words.append("spam")
words.append("foo")
words.append("bar")

counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 2:
        break
    
print("Let u try to delete something that isn't in the list.")
words.delete('socks')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 4:
        break
    
print("Let us delete something that is there.")
words.delete('foo')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 3:
        break
        
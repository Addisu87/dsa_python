
# nodes and pointers
class Node: 
  def __init__ (self, data=None):
    self.data = data
    self.next = None
  
class SinglyLinkedList:
  def __init__(self):
    self.tail = None
    self.head = None
    self.size = 0
  
  # inserting items
  
  def append(self, data):
  # appending items to the end of a list
    node = Node(data)
    # encapsulate the data in a Node
    if self.tail:
      self.tail.next = node
      self.tail = node 
    else: 
     self.head = node
     self.tail = node
       
  def append_at_a_location(self, data, index):
      # appending items at intermediate positions
      current = self.head
      prev = self.head
      node = Node(data)
      count = 1
      
      while current: 
        if count == 1:
          node.next = current
          self.head = node
          print(count)
          return 
        elif index == index:
          node.next = current
          prev.next = node
          return
        else:
          count += 1
          prev = current
          current = current.next
      
      if count < index: 
        print("The list has less number of elements")
        
  def append_at_same_location(self, data):
  #  to insert a new element just before an element that has the same data value.
    current = self.head
    prev = self.head
    node = Node(data)
    
    while current:
        if current.data == data:
            node.next = current
            prev.next = node
        prev = current
        current = current.next
        
  
  # querying a list
  # traversing a list

  def iter(self):
  # improving list creation and traversal
    current = self.head
    
    while current:
      val = current.data
      current = current.next
      yield val
      
  
  def search(self, data):
  # searching an element in a list
      for node in self.iter():
        if data == node:
          return True
        
      return False
    
    
  # deleting items
  
  def delete_first_node(self):
  # deleting the node at the beginning of the singly linked list
    current = self.head
    
    if self.head is None:
      print("No data element to delete")
    elif current == self.head:
      self.head = current.next
      
  def delete_last_node(self):
  # Deleting the node at the end in the singly linked list
    current = self.head
    prev = self.head
    
    while current: 
      if current.next is None:
        prev.next = current.next
        self.size -= 1
        
      prev = current
      current = current.next
      
      
  def delete(self, data):
  # deleting any intermediate node in a singly linked list
    current = self.head
    prev = self.head
    
    while current:
        if current.data == data:
          if current == self.head:
            self.head = current.next
          else: 
            prev.next = current.next
          self.size -= 1
          return
        
        prev = current
        current = current.next
        
        
    # clearing a list
    
  def clear(self):
    # Clear the entire list.
    self.tail = None
    self.head = None
    

# appending items to the end of a list    
words = SinglyLinkedList()
print("Append an element at the end location:")
words.append('egg')
words.append('ham')
words.append('spam')
current = words.head
while current:
    print(current.data)
    current = current.next
 
print("Traversing elements:")
# list traversal 
for word in words.iter():
  print(word)
  
         
# insert a new node at an intermediate position
print("Append an element at a specific location:")
words.append_at_a_location("new", 2)
current = words.head
while current:
  print(current.data)
  current = current.next 
  
  
# appending items to the end of same location         
# insert a new node at an intermediate same position
print("Append an element at the same location of existing element:")
words.append_at_same_location("ham")
current = words.head
while current:
  print(current.data)
  current = current.next 
  
# querying a list
# for searching a given data item
print("Search specific element:")
print(words.search('sspam'))
print(words.search('egg'))


print("Delete an element at first node location:")
# deleting the node at the begging
words.delete_first_node()
current = words.head
while current:
  print(current.data)
  current = current.next

print("Delete a specific element:")
# deleting data element at the intermediate position
words.delete("ham")
current =  words.head
while current:
  print(current.data)
  current = current.next
  
print("Clear elements:")
# clearing items
words.clear()
          
   
   

  




# implementation of the hash table with separate chaining
# use a binary search tree to avoid the slow retrieval of items, and 
# BST is self-balancing

class Node:
   def __init__(self, key=None, value=None):
      self.key = key
      self.value = value
      self.next = None
      
class SinglyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
      
   def append(self, key, value):
      new_node = Node(key, value)
      if self.tail:
         self.tail.next = new_node
         self.tail = new_node
      else: 
         self.head = new_node
         self.tail = new_node
         
   def traverse(self):
      current = self.head
      while current:
         print("\"", current.key, "__", current.value, "\"")
         current = current.next
         
   def search(self, key):
      current = self.head
      while current:
         if current.key == key:
            print("\"Record found:", current.key, "-", current.value, "\"")
            
            return True
         current = current.next
      return False
 
  
class HashTableChaining:
   def __init__(self):
      self.size = 6
      self.slots = [None for _ in range(self.size)]
      
      for x in range(self.size):
         self.slots[x] = SinglyLinkedList()
         
   def _hash(self, key):
      mult = 1
      hv = 0
      for ch in key:
         hv += mult * ord(ch)
         mult += 1
      return hv % self.size
   
   def put(self, key, value):
      h = self._hash(key)
      self.slots[h].append(key, value)
      
   def get(self, key):
      h = self._hash(key)
      v = self.slots[h].search(key)
      
   def printHashTable(self):
      print("Hash table is :- \n")
      print("Index \t\tValues\n")
      for x in range(self.size):
         print(x, end="\t\n")
         self.slots[x].traverse()
         
         
my_ht = HashTableChaining()
my_ht.put("good", "eggs")
my_ht.put("better", "ham")
my_ht.put("best", "spam")
my_ht.put("ad", "do not")
my_ht.put("ga", "collide")
my_ht.put("awd", "do not")

print(my_ht.printHashTable())
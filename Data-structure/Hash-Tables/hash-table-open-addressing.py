

# Implementing hash tables
# Creating a class to hold hash table items
class HashItem:
   def __init__(self, key, value):
      self.key = key
      self.value = value
      
class HashTable:
   def __init__(self):
      self.size = 256
      self.slots = [None for _ in range(self.size)]
      self.count = 0
      self.MAXLOADFACTOR = 0.65
      self.prime_num = 5
   
   # Collision solving techniques
   
   # 1- Linear probing to resolve collisions
   # the addition and retrieval of data elements
      
   # we use underscore to use for internal use only
   # generate the hash value for a string
   # compute the sum of the ordinal values
   def _hash(self, key):
      mult = 1
      hv = 0
      for ch in key:
         hv += mult * ord(ch)
         mult += 1
      return hv % self.size
   
   # compute the sum of the ordinal values
   # since we have strings as a key element
   def h2(self, key):
      mult = 1
      hv = 0
      for ch in key:
         hv += mult * ord(ch)
         mult += 1
      return hv

   # Storing elements in a hash table
   def put(self, key, value):
      item = HashItem(key, value)
      h = self._hash(key)
      # if the slot is not empty,
      # the next free slot is checked by adding 1
      while self.slots[h] != None:
         if self.slots[h].key == key:
            break
         h = (h + 1) % self.size
      if self.slots[h] is None:
         self.count += 1
      self.slots[h] = item
      self.check_growth()
      

   # check the load factor of the hash table 
   # after adding any record to the hash table
   def check_growth(self):
      load_factor = self.count / self.size
      if load_factor > self.MAXLOADFACTOR:
         print("Load factor before growing the hash table", self.count / self.size)
         self.growth()
         print("Load factor after growing the hash table", self.count / self.size)
     
   # Growing a hash table
   # expand the size of the hash table 
   # when we have a very limited number of empty slot    
   def growth(self):
      New_Hash_Table = HashTable()
      New_Hash_Table.size = 2 * self.size
      New_Hash_Table.slots = [None for _ in range(New_Hash_Table.size)]
      
      for i in range(self.size):
         if self.slots[i] != None:
            New_Hash_Table.put(self.slots[i].key, self.slots[i].value)
      
      self.size = New_Hash_Table.size
      self.slots = New_Hash_Table.slots
      
   # Retrieving elements from the hash table
   def get(self, key):
      h = self._hash(key) # computed hash for the given key
      while self.slots[h] != None:
         if self.slots[h].key == key:
            return self.slots[h].value
         h = (h + 1) % self.size 
      return None
   
   # Implementing a hash table as a dictionary
   # using special methods, __setitem__() and __getitem__()
   def __setitem__(self, key, value):
      self.put(key, value)
      
   def __getitem__(self, key):
      return self.get(key)
   
   # 2- Quadratic probing
   # using a quadratic polynomial
   def put_quadratic(self, key, value):
      item = HashItem(key, value)
      h = self._hash(key)
      j = 1
      while self.slots[h] != None:
         if self.slots[h].key == key:
            break
         h = (h + j*j) % self.size
         j = j + 1
         
      if self.slots[h] is None:
         self.count += 1
      self.slots[h] = item
      self.check_growth()
      
   def get_quadratic(self, key):
      h = self._hash(key)
      j = 1
      while self.slots[h] != None:
         if self.slots[h].key == key:
            return self.slots[h].value
         h = (h + j*j) % self.size
         j = j + 1   
      return None
   
   
   # 3- Double hashing
   def put_double_hashing(self, key, value):
      item = HashItem(key, value)
      h = self._hash(key)
      j = 1
      while self.slots[h] != None:
         if self.slots[h].key == key:
            break
         h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
         j = j + 1
      
      if self.slots[h] is None:
         self.count += 1
      self.slots[h] = item
      self.check_growth()
      
   def get_double_hashing(self, key):
      h = self._hash(key)
      j = 1
      while self.slots[h] != None:
         if self.slots[h].key == key:
            return self.slots[h].value
         h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
         j = j + 1   
      return None
   
   

my_hash_table = HashTable()

# Test linear probing
# my_hash_table.put("good", "eggs")
# my_hash_table.put("better", "ham")
# my_hash_table.put("best", "spam")
# my_hash_table.put("ad", "do not")
# my_hash_table.put("ga", "collide")

# print(my_hash_table.check_growth())
# for key in ("good", "better", "best", "worst", "ad", "ga"):
#    val = my_hash_table.get(key)
#    print(val)

# Test implementation using dictionaries
# my_hash_table["good"] = "eggs"
# my_hash_table["better"] = "ham"
# my_hash_table["best"] = "spam"
# my_hash_table["ad"] = "do not"
# my_hash_table["ga"] = "collide"

# for key in ("good", "better", "best", "worst", "ad", "ga"):
#    val = my_hash_table[key]
#    print(val)
   
# print("The number of elements is: {}".format(my_hash_table.count))


# Test quadratic probing
# my_hash_table.put_quadratic("good", "eggs")
# my_hash_table.put_quadratic("ad", "packt")
# my_hash_table.put_quadratic("ga", "books")

# v = my_hash_table.get_quadratic('ga')
# print(v)

# Testing double hashing

my_hash_table.put_double_hashing("good", "eggs")
my_hash_table.put_double_hashing("better", "spam")
my_hash_table.put_double_hashing("best", "cool")
my_hash_table.put_double_hashing("ad", "do not")
my_hash_table.put_double_hashing("ga", "collide")
my_hash_table.put_double_hashing("awd", "hello")
my_hash_table.put_double_hashing("addition", "ok")

for key in ("good", "better", "best", "worst", "ad", "ga"):
   val = my_hash_table.get_double_hashing(key)
   print(val)
   
print("The number of elements is: {}".format(my_hash_table.count))

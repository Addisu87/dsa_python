# Binary Search Tree(BST)
class Node:
   def __init__(self, value):
      self.value = value
      self.left_child = None
      self.right_child = None
      
class BinarySearchTree:
   def __init__(self):
      self.root_node = None
      
   # tree traversal algorithm, in-order tree traverse
   def in_order(self, root_node):
      current = root_node
      if current is None:
         return 
      self.in_order(current.left_child)
      print(current.value)
      self.in_order(current.right_child)
      
   # BST operations
   # 1- Insert method to add the nodes in the binary search tree
   def insert(self, value):
      new_node = Node(value)
      if self.root_node is None:
         self.root_node = new_node
         return self.root_node
      else:
         current = self.root_node
         parent = None
         while True:
            parent = current
            if new_node.value < parent.value:
               current = current.left_child
               if current is None:
                  parent.left_child = new_node
                  return self.root_node
            else:
               current = current.right_child
               if current is None:
                  parent.right_child = new_node
                  return self.root_node
               
   # 2- Searching the tree
   def search(self, value):
      current = self.root_node
      while True:
         if current is None:
            print("Item not found")
            return None
         elif current.value is value:
            print("Item found", value)
            return value
         elif current.value > value:
            current = current.left_child 
         else:
            current = current.right_child 
            
   # 3- Deleting nodes
   # write a helper method to get the node that we want to delete
   # along with the reference to its parent node
   def get_node_with_parent(self, value):
      parent = None
      current = self.root_node
      if current is None:
         return (parent, current)
      
      while True:
         if current.value == value:
            return (parent, current)
         elif current.value > value:
            parent = current
            current = current.left_child
         else:
            parent = current
            current = current.right_child
      return (parent, current)
         
   def remove(self, value):
      parent, node_rmv = self.get_node_with_parent(value)
      
      if parent is None and node_rmv is None:
         return False
      
      # Get children count
      children_count = 0
      
      # number of children a node has that we want to delete
      if node_rmv.left_child and node_rmv.right_child:
         children_count = 2
      elif (node_rmv.left_child is None) and (node_rmv.right_child is None):
         children_count = 0
      else:
         children_count = 1
      
      #  the case where the node has no children 
      if children_count == 0:
         if parent:
            if parent.right_child is node_rmv:
               parent.right_child = None
            else:
               parent.left_child = None
         else:
            self.root_node = None
       # the case where the node has 1 children    
       # next_node is used to keep track of that single node,
       # which is the child of the node that is to be deleted 
      elif children_count == 1:
         next_node = None
         if node_rmv.left_child:
            next_node = node_rmv.left_child
         else:
            next_node = node_rmv.right_child
            
         if parent:
            if parent.left_child is node_rmv:
               parent.left_child = next_node
            else:
               parent.right_child = next_node
         else:
            self.root_node = next_node      
      #  the case where the node has 2 children  
      else:
         parent_of_leftmost_node = node_rmv
         leftmost_node = node_rmv.right_child
         while leftmost_node.left_child:
            parent_of_leftmost_node = leftmost_node
            leftmost_node = leftmost_node.left_child
         # update the node that’s about to be removed with the value
         node_rmv.value = leftmost_node.value
         
         if parent_of_leftmost_node.left_child == leftmost_node:
            parent_of_leftmost_node.left_child = leftmost_node.right_child
         else:
            parent_of_leftmost_node.right_child = leftmost_node.right_child   
            
            
   # Finding the minimum and maximum nodes
   
   # finding the minimum value of any node
   def find_min(self):
      current = self.root_node
      while current.left_child:
         current = current.left_child
         
      return current.value
   
   # finding the maximum node
   def find_max(self):
      current = self.root_node
      while current.right_child:
         current = current.right_child
      
      return current.value
            
               
bst = BinarySearchTree()
 
ins = bst.insert(5)
ins = bst.insert(2)
ins = bst.insert(7)
ins = bst.insert(9)
ins = bst.insert(1)
               
# bst.in_order(ins)
bst.search(9)
# bst.remove(9)
# bst.search(9)

print(bst.find_min())
print(bst.find_max())
               
   
   
   
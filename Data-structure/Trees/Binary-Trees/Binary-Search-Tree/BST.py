class Node:
    def __init__(self, value):
        self.value = value  # set the value of the node
        self.left = None  # set the left child to None
        self.right = None  # set the right child to None


class BinarySearchTree:
    # constructor for the binary search tree
    def __init__(self):
        self.root = None   # set the root of the tree to None

    # Insert method - iteratively
    def insert(self, value):
        # create a new node with the given value
        new_node = Node(value)
        # if the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return True
        # set a temporary node to the root of the tree
        temp = self.root
        while (True):
            # if the value already exists in the tree, return False
            if new_node.value == temp.value:
                return False
            # if the value is less than the temporary node's value, go left
            if new_node.value < temp.value:
                # if there's no left child, insert the new node as the left child
                if temp.left is None:
                    temp.left = new_node
                    return True
                # otherwise, continue iterating through the left subtree
                temp = temp.left
            # if the value is greater than the temporary node's value, go right
            else:
                # if there's no right child, insert the new node as the right child
                if temp.right is None:
                    temp.right = new_node
                    return True
                # otherwise, continue iterating through the right subtree
                temp = temp.right

    # contains method - iteratively
    def contains(self, value):
        # start at the root of the tree
        temp = self.root
        # iterate through the tree until the node
        # is found or the end of the tree is reached
        while temp is not None:
            # if the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left
            # if the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            # if the value matches the current node's value, return True
            else:
                return True
        # if the value is not found in the tree, return False
        return False

    # contains method - recursively
    #  a private recursive helper method
    def __r_contains(self, current_node, value):
        # If current_node is None, we have reached a leaf node and
        # the value is not present in the tree.
        if current_node == None:
            return False
        # If the value matches the value of the current_node,
        # we have found the value and return True.
        if value == current_node.value:
            return True
        # If the value is less than the value of the current_node,
        # we recurse on the left subtree.
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        # If the value is greater than the value of the current_node,
        # we recurse on the right subtree.
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    # calling method
    def r_contains(self, value):
        # The r_contains method calls the private helper method __r_contains
        # with the root node of the tree and the value to search for.
        # It returns the output of __r_contains.
        return self.__r_contains(self.root, value)

    # Recursively - Insert method
    # a private recursive helper method
    def __r_insert(self, current_node, value):
        # If current_node is None, we have reached a leaf node and
        # insert a new node with the given value.
        if current_node == None:
            return Node(value)
        # If the value is less than the value of the current_node,
        # we insert the value into the left subtree.
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
          # If the value is greater than the value of the current_node,
          # we insert the value into the right subtree.
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        # Return the modified current_node after inserting the value.
        return current_node

    # calling method
    def r_insert(self, value):
        # If the tree is empty, create a new node and make it the root node.
        if self.root == None:
            self.root = Node(value)
        # Call the private helper method __r_insert with the root node and
        # the value to be inserted.
        self.__r_insert(self.root, value)

    # find the minimum value
    def find_min(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.value

    # find the maximum value
    def find_max(self):
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.value

    # Delete method - Recursively

    # A helper method - finding the minimum value
    def min_value(self, current_node):
        # Iterate until no left child is found
        while current_node.left is not None:
            # Move to the left child of current node
            current_node = current_node.left
        # Return the value of the leftmost node
        return current_node.value

    # delete method
    def __delete_node(self, current_node, value):
        # Return None if the current node is None
        if current_node == None:
            return None
        # Traverse the left subtree if value is smaller
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        # Traverse the right subtree if value is larger
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # If value is found, delete the node
        else:
            # case-1: it is a leaf node (No children, return None to delete)
            if current_node.left == None and current_node.right == None:
                return None
            # Case-2: No left child, return right child
            elif current_node.left == None:
                current_node = current_node.right
            # Case-3: No right child, return left child
            elif current_node.right == None:
                current_node = current_node.left
            # Case-4: Two children, find min in right subtree
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min)
        # Return the current node after deletion
        return current_node

    # Calling method
    def delete_node(self, value):
        # Call the helper method to delete the node
        self.__delete_node(self.root, value)

   # Tree Traversal
    # Breadth-first traversal(BFS)

   # YOU CAN WRITE BFS WITH A QUEUE INSTEAD OF LIST
   # (TECHNICALLY THIS IS A BETTER SOLUTION)

    def BFS(self):
        # set current_node to the root of the tree
        current_node = self.root
        # create an empty queue to store nodes to visit
        queue = []
        # create an empty list to store the values of visited nodes
        results = []
        # add the root node to the queue
        queue.append(current_node)
        # continue until all nodes have been visited
        while len(queue) > 0:
           # remove the first node from the queue
            current_node = queue.pop(0)
            # add the value of the visited node to the results list
            results.append(current_node.value)
            # if the visited node has a left child, add it to the queue
            if current_node.left is not None:
                queue.append(current_node.left)
            # if the visited node has a right child, add it to the queue
            if current_node.right is not None:
                queue.append(current_node.right)
        # return the list of visited node values
        return results

   # Depth First Search(DFS)
   # DFS pre-order (Root-Left-Right)

    def dfs_pre_order(self):
       # create an empty list to store the values of visited nodes
        results = []

        def traverse(current_node):
           # append the value of the current node to the results list
            results.append(current_node.value)
            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)
            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)

        # start the pre-order traversal from the root of the tree
        traverse(self.root)
        # return the list of visited node values
        return results

   #  DFS post-order traversal(Left-Right-Root)
    def dfs_post_order(self):
        # create an empty list to store the values of visited nodes
        results = []

        def traverse(current_node):
            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)
            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)
            # append the value of the current node to the results list
            results.append(current_node.value)
        # start the post-order traversal from the root of the tree
        traverse(self.root)
        # return the list of visited node values
        return results

   # In-order traversal(Left-Root-Right)
    def dfs_in_order(self):
       # create an empty list to store the values of visited nodes
        results = []

        def traverse(current_node):
            # if the current node has a left child, recursively traverse it
            if current_node.left is not None:
                traverse(current_node.left)
            # append the value of the current node to the results list
            results.append(current_node.value)
            # if the current node has a right child, recursively traverse it
            if current_node.right is not None:
                traverse(current_node.right)
         # start the in-order traversal from the root of the tree
        traverse(self.root)
        # return the list of visited node values
        return results

   # BST: Validate BST (⚡Interview Question)
   # You are tasked with writing a method called is_valid_bst in the BinarySearchTree
   # class that checks whether a binary search tree is a valid binary search tree.
    def is_valid_bst(self):
       # Get node values of the binary search tree in ascending order
        node_values = self.dfs_in_order()
        # Iterate through the node values using a for loop
        for i in range(1, len(node_values)):
            # Check if each node value is greater than the previous node value
            if node_values[i] <= node_values[i - 1]:
                # If node values are not sorted in ascending order, the binary
                # search tree is not valid, so return False
                return False
         # If all node values are sorted in ascending order, the binary search tree
         # is a valid binary search tree, so return True
        return True

   # BST: Kth Smallest Node
   # Given a binary search tree, find the kth smallest element in the tree.
   # For example, if the tree contains the elements [1, 2, 3, 4, 5],
   # the 3rd smallest element would be 3.

   # solution-1: Iterative approach using a stack
    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []
        # start at the root of the tree
        temp = self.root

        while stack or temp:
            # traverse to the leftmost node
            while temp:
               # add the node to the stack
                stack.append(temp)
                temp = temp.left
            # pop the last node added to the stack
            temp = stack.pop()
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:
                return temp.value
            # move to the right child of the node
            node = node.right
         # if k is greater than the number of nodes in the tree, return None
        return None

     #  solution-2: Recursive solution
    def kth_smallest(self, k):
        #  initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        #  call the helper function with the root node and k
        return self.kth_smallest_helper(self.root, k)

    def kth_smallest_helper(self, temp, k):
        if temp is None:
         #  if the current node is None, return None
            return None

        # recursively call the helper function on the left child of the node and
        # store the result in left_result
        left_result = self.kth_smallest_helper(temp.left, k)
        if left_result is not None:
            #  if left_result is not None, return it
            return left_result

         # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            #  if the kth smallest element is found, return the value of the current node
            return temp.value

        # recursively call the helper function on the right child of the node and
        # store the result in right_result
        right_result = self.kth_smallest_helper(temp.right, k)
        if right_result is not None:
            #  if right_result is not None, return it
            return right_result
         #  if the kth smallest element is not found, return None
        return None


# Invoke the BST function
my_tree = BinarySearchTree()

# print(my_tree.root)

# Insert values iteratively
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


# print('Root:', my_tree.root.value)
# print('Root->Left:', my_tree.root.left.value)
# print('Root->Right:', my_tree.root.right.value)

# Insert values recursively
# my_tree.r_insert(2)
# my_tree.r_insert(1)
# my_tree.r_insert(3)

# print('Root:', my_tree.root.value)
# print('Root->Left:', my_tree.root.left.value)
# print('Root->Right:', my_tree.root.right.value)

# # Check values contains/searching iteratively
# print('BST Contains 27:')
# print(my_tree.contains(27))

# print('\nBST Contains 17:')
# print(my_tree.contains(17))


# Check values contains/searching recursively
# print('\nBST Contains 27:')
# print(my_tree.r_contains(27))

# print('\nBST Contains 17:')
# print(my_tree.r_contains(17))


# print('\nBST min_value:')
# print(my_tree.find_min())

# print('\nBST max_value:')
# print(my_tree.find_max())


# Finding the minimum value
# print(my_tree.min_value(my_tree.root))

# print(my_tree.min_value(my_tree.root.right))


# To delete recursively
# my_tree.delete_node(2)

# print("\nroot:", my_tree.root.value)
# print("root.left =", my_tree.root.left.value)
# print("root.right= ", my_tree.root.right)


# Tree Traversal
# print(my_tree.BFS())

# dfs of pre_order (Root -> Left -> Right)
print(my_tree.dfs_pre_order())

# dfs of post_order (Left -> Right -> Root)
print(my_tree.dfs_post_order())

# dfs of in_order (Left -> Root -> Right)
print(my_tree.dfs_in_order())

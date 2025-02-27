# Create a binary tree Node class
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def print_traverse(self):
        current = n1
        while current:
            print(current.value)
            current = current.left_child


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


node = Node(n1)
node.print_traverse()
print("Node" "\n")


# Tree traversal

# 1-In-order traversal(Left-Root-Right)
# We start traversing the left subtree and call an
# ordering function recursively
# Next, we visit the root node
# Finally, we traverse the right subtree and call an
# ordering function recursively
def in_order(root_node):
    current = root_node
    if current is None:
        return
    in_order(current.left_child)
    print(current.value)
    in_order(current.right_child)


print(in_order(n1), "\n")

# 2-pre-order traversal(Root-Left-Right)
# We start traversing with the root node
# Next, we traverse the left subtree and call an ordering function
# with the left subtree recursively
# Next, we visit the right subtree and call an ordering function
# with the right subtree recursively


def pre_order(root_node):
    current = root_node
    if current is None:
        return
    print(current.value)
    pre_order(current.left_child)
    pre_order(current.right_child)


print(pre_order(n1), "\n")

# 3-post-order traversal(Left-Right-Root)
# We start traversing the left subtree and call an
# ordering function recursively
# Next, we traverse the right subtree and call an
# ordering function recursively
# Finally, we visit the root node


def post_order(root_node):
    current = root_node
    if current is None:
        return
    post_order(current.left_child)
    post_order(current.right_child)
    print(current.value)


print(post_order(n1), "\n")


# Breadth-first traversal
# Level order traversal


def level_order_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])

    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.value)
        if node.left_child:
            traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)

    return list_of_nodes


print(level_order_traversal(n1), "\n")

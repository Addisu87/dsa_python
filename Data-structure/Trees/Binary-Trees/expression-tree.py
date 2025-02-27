# Expression trees - arithmetic expressions
# The arithmetic expression is shown using three notations:
# infix, postfix, or prefix. 

# Parsing a reverse Polish expression
# To create an expression tree from the postfix notation,
# a stack is used.

class TreeNode:
   def __init__(self, value=None):
      self.value = value
      self.right = None
      self.left = None
      
class Stack:
   def __init__(self):
      self.elements = []
      
   def push(self, item):
      self.elements.append(item)
      
   def pop(self):
      return self.elements.pop()
   
   
expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
   if term in "+-*/":
      node = TreeNode(term)
      node.right = stack.pop()
      node.left = stack.pop()
   else:
      node = TreeNode(int(term))
   stack.push(node)
   
   
def calc(node):
   if node.value == "+":
      return calc(node.left) + calc(node.right)
   elif node.value == "-":
      return calc(node.left) - calc(node.right)
   elif node.value == "*":
      return calc(node.left) * calc(node.right)
   elif node.value == "/":
      return calc(node.left) / calc(node.right)
   else:
      return node.value
   
root = stack.pop()
result = calc(root)
print(result)
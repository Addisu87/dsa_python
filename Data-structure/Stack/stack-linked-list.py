# Holds data and
# Reference to the next item in the LL.
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
class Stack:
   # Initialized the Stack class
   def __init__ (self):
      self.data = None
      self.top = None
      self.size = 0
      
   def print_stack(self):
      current = self.top
      while current:
         print(current.data) 
         current = current.next
      
   # push operation
   # to add element at the top 
   def push(self, data):
      # create a new node and store data
      new_node = Node(data)
      
      if self.top:
         new_node.next = self.top
         self.top = new_node
      else:
         self.top = new_node
      self.size += 1
      
   def pop(self):
      # remove the topmost element
      if self.top:
         data = self.top.data
         self.size -= 1
         if self.top.next: #check if there is more than one node
            self.top = self.top.next
         else:
            self.top = None
         return data
      else:
         print("Stack is empty")
         
   def peek(self):
      # to read the topmost element
      if self.top:
         return self.top.data
      else:
         print("Stack is empty")
  
   # print the stack elements.
words = Stack()
words.push("egg")
words.push("ham")
words.push("spam")

words.pop()

words.peek()

words.print_stack()

# Applications of stacks       
# Bracket matching utilizing stacks
def check_brackets(expression):
   brackets_stack = Stack()
   
   last = ' '
   for ch in expression:
      if ch in ('{', '[', '('):
         brackets_stack.push(ch)
      
      if ch in ('}', ']', ')'):
         last = brackets_stack.pop()
         
         if last == '{' and ch == '}':
            continue
         elif last == '[' and ch == ']':
            continue
         elif last == '(' and ch == ')':
            continue
         else:
            return False
   if brackets_stack.size > 0:
      return False
   else:
      return True
 
   
sl = (
   "{(foo)(bar)}[hello](((this)is)a)test",
   "{(foo)(bar)}[hello](((this)is)atest",
   "{(foo)(bar)}[hello](((this)is)a)test))"    
)

for s in sl:
      m = check_brackets(s)
      print("{}: {}".format(s, m))
      

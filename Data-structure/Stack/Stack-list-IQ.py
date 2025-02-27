# Stack implementation using lists

class Stack:
   def __init__(self):
      self.stack_list = []

   # to print the results 
   def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])
   
   # check if the list is empty 
   def is_empty(self):
        return len(self.stack_list) == 0

   # read the last element using peek method
   def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
      
   # check the size of the list
   def size(self):
        return len(self.stack_list)

   # push method
   def push(self, value):
        self.stack_list.append(value)
    
   #  pop method
   def pop(self):
      if self.is_empty():
         return None
      else:
         return self.stack_list.pop()
      
   
my_stack = Stack()
my_stack.push(3)
my_stack.push(5)
my_stack.push(4)
my_stack.push(1)
my_stack.push(2)

print("Stack before pop():")
my_stack.print_stack()

# print("\nPopped node:")
# print(my_stack.pop())

# print("\nStack after pop():")
# my_stack.print_stack()



# Application of Stack

# Qn. Parentheses Balanced (⚡Interview Question)
# Check to see if a string of parenthesis is balanced or not.

def is_balanced_parentheses(parentheses):
    stack = Stack()
    
    for par in parentheses:
        if par == '(':
            stack.push(par)
        elif par == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
             
    return stack.is_empty()
         
balanced_parenthesis = "((()))"
unbalanced_parenthesis = "((())))"

print(is_balanced_parentheses(balanced_parenthesis))
print(is_balanced_parentheses(unbalanced_parenthesis))

# Qn.Reverse string (⚡Interview Question)
def reverse_string(string):
   # create a new stack
   stack = Stack()
   # create an empty string to store the reversed string
   reversed_string = ""
   
   # push each character in the string onto the stack
   for char in string:
      stack.push(char)
      
   # pop each character off the stack and append it to the reversed string
   while not stack.is_empty():
      reversed_string += stack.pop()
      
   # return the reversed string
   return reversed_string


my_string = "hello"

print(reverse_string(my_string))


# Qn. Sort Stack (⚡Interview Question)
# sorts a given stack of integers in ascending order 

def sort_stack(stack):
   # Create a new stack to hold the sorted elements
   add_stack = Stack()

   # While the original stack is not empty
   while not stack.is_empty():
      # Remove the top element from the original stack
      temp = stack.pop()
      
      # while the additional stack is not empty and 
      # the top element is greater than the current element
      while not add_stack.is_empty() and add_stack.peek() > temp:
         # Move the top element from the additional stack to the original stack
         stack.push(add_stack.pop())
         
      # Add the current element to the additional stack
      add_stack.push(temp)
      
   # Copy the sorted elements from the additional stack to the original stack
   while not add_stack.is_empty():
      stack.push(add_stack.pop())
      
      
print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()





# Stack implementation using arrays

# Implementation of push method
size = 3
data = [0] * (size) # Initialize the stack
top = -1

def push(x):
   global top
   if top >= size - 1:
         print("Stack Overflow")
   else:
         top = top + 1
         data[top] = x

# insert data elements
push("egg")
push("ham")
push("spam")

push(data[0 : top + 1])

push("new")
push("new2")

# Implementation of pop method
def pop():
   global top
   if top == -1:
      print("Stack Underflow")
   else:
      top = top - 1
      data[top] = 0
      return data[top + 1]

print(data[0 : top + 1])

pop()
pop()
pop()
pop()

print(data[0 : top + 1])

# Implementation of peek method
def peek():
   global top
   if top == -1:
      print("Stack is empty")
   else:
      print(data[top])
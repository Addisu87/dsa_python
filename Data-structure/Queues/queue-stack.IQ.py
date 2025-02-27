# Applications of Queue using stacks

class MyQueue:
   def __init__(self):
      self.stack1 = []
      self.stack2 = []
      
   def is_empty(self):
      return len(self.stack1) == 0
   
   def peek(self):
      return self.stack1[-1]
   
# Queue Using Stacks: Enqueue (⚡Interview Question)
# You are given a class MyQueue which implements a queue using two stacks.
# Your task is to implement the enqueue method which should add an element
# to the back of the queue.

   def enqueue(self, value):
      # Transfer all elements from stack1 to stack2
      while len(self.stack1) > 0:
         self.stack2.append(self.stack1.pop())
      
      # Add the new element to the bottom of stack1
      self.stack1.append(value)
      
      # Transfer all elements back from stack2 to stack1
      while len(self.stack2) > 0:
         self.stack1.append(self.stack2.pop())
         
         
# Queue Using Stacks: Dequeue (⚡Interview Question)
# You have been tasked with implementing a queue data structure using 
# two stacks in Python, and you need to write the dequeue method.
   
   def dequeue(self):
      # Check if the queue is empty
      if self.is_empty():
         # Return None if the queue is empty
         return None
      else:
         # Remove and return the last element in stack1
         # Which is the first element in the queue
         return self.stack1.pop()
   
   
# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Enqueue another value
q.enqueue(4)

# Output the front of the queue again
print("Front of the queue:", q.peek())

# Dequeue all remaining values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

# Dequeue from an empty queue and check if it returns None
print("Dequeued value from empty queue:", q.dequeue())
      
   
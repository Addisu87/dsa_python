# Fibonacci series can be demonstrated using a recurrence relation

def fib(n):
  if n <= 1:
    return 1
  
  else: 
    return fib(n - 1) + fib(n - 2)
  
# example

for i in range(5):
  print(fib(i))
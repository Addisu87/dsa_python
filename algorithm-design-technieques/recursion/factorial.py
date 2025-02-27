# Recursion algorithm design techniques
# Recursion - is a function that calls itself until it doesn't.

# Example - factorial
def factorial(n):
  # test for a base case
  if n == 1:
    return 1
  # make a calculation and a recursion call
  return n * factorial(n -1)

print(factorial(4))
  
  
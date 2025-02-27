# Set: Find Pairs (⚡Interview Question)
# You are given two lists of integers, arr1 and arr2, and
# a target integer value, target. Your task is to find all pairs
# of numbers (one from arr1 and one from arr2) whose sum equals target.

# Write a function called find_pairs that takes in three 
# arguments: arr1, arr2, and target, and returns a list of all such pairs.

def find_pairs(arr1, arr2, target):
   # Convert arr1 to a set for O(1) lookup
   set_one = set(arr1)
   # Initialize an empty list to store the pairs
   pairs = []
   
   # loop through each number in arr2
   for num in arr2:
      # Calculate the complement of the current number
      complement = target - num
      # Check if the complement is in set1
      if complement in set_one:
         # If it is, add the pair to the pairs list(as tuple)
         pairs.append((complement, num))
         
   # Return the list of pairs that add up to the target value
   return pairs
   
   
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
# HT: Two Sum (⚡Interview Question)

# Problem: Given an array of integers nums and a target integer target,
# find the indices of two numbers in the array that add up to the target.

def two_sum(nums, target):
   # create an empty hash table
   num_map = {}
   
   # iterate through each number in the array
   for i, num in enumerate(nums):
      # calculate the complement of the current number
      complement = target - num 
      
      # check if the complement is in the hash table
      if complement in num_map:
         # if it is, return the indices of the two numbers
         return [num_map[complement], i]
      
      # add the current number and its index to the hash table
      num_map[num] = i
      
   # if no two numbers add up to the target, return an empty list
   return []


print ( two_sum([2, 7, 11, 15], 9) )
print ( two_sum([3, 2, 4], 6) )
print ( two_sum([3, 3], 6) )
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )

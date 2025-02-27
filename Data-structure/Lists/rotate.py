# Instructions:
# List: Rotate (⚡Interview Question)
# You are given a list of n integers and a non-negative integer k.
# Your task is to write a function called rotate that takes the list
# of integers and an integer k as input and rotates the list to the
# right by k steps.

# The function should modify the input list in-place, and
# you should not return anything.

# Constraints:
# Each element of the input list is an integer.
# The integer k is non-negative.

def rotate(nums, k):
   # Calculate the effective number of steps to rotate
    k = k % len(nums)
   #  Rearrange the elements in the rotated order by
   #  slicing and concatenating them in reverse order
    nums[:] = nums[-k:] + nums[:-k]

# Example


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)

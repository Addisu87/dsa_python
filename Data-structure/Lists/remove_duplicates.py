# List: Remove Duplicates (⚡Interview Question)
# Given a sorted list of integers, rearrange the list in-place such that all
# unique elements appear at the beginning of the list, followed by the duplicate elements.
# Your function should return the new length of the list containing only unique elements.


# Constraints:
# The input list is sorted in non-decreasing order.
# The input list may contain duplicates.
# The function should have a time complexity of O(n),
# where n is the length of the input list.
# The function should have a space complexity of O(1), i.e.,
# it should not use any additional data structures or create new lists.

def remove_duplicates(nums):
   # Return zero if input is empty
    if not nums:
        return 0
   # Initialize write_pointer at index 1
    write_pointer = 1
   #  Loop through list starting from index 1
    for read_pointer in range(1, len(nums)):
      #  Check if current element is unique
        if nums[read_pointer] != nums[read_pointer - 1]:
           # Move unique element to write_pointer
            nums[write_pointer] = nums[read_pointer]
            # Increment write_pointer for next unique element
            write_pointer += 1
   #  Return new length of list with unique elements
    return write_pointer


# Example
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])

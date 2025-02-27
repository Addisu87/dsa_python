# List: Find Max Min (⚡Interview Question)
# Write a Python function that takes a list of integers as input and
# returns a tuple containing the maximum and minimum values in the list.

def find_max_min(myList):
   # Initialize the maximum and minimum variables
   # to the first element of the list
    maximum = minimum = myList[0]
   # Traverse the list and update the
   # maximum and minimum variables
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    # Return the maximum and minimum variables
    return maximum, minimum


# example
print(find_max_min([5, 3, 8, 1, 6, 9]))

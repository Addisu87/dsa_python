# Quick sort algorithm
# Helper function to swap values
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# to get a pivot point
def pivot(my_list, pivot_index, end_index):
   # initialize the swap index to the pivot index
    swap_index = pivot_index
   # iterate over the list from the pivot index + 1 to the end index
    for i in range(pivot_index + 1, end_index + 1):
      #  if the current element is less than the pivot element
        if my_list[i] < my_list[pivot_index]:
            #  increment the swap index
            swap_index += 1
            # swap the current element with the element at the swap index
            swap(my_list, swap_index, i)
   # swap the pivot element with the element at the swap index
    swap(my_list, pivot_index, swap_index)
   # return the index of the pivot element after swapping
    return swap_index

# Apply quick sort after getting a pivot point
# to eliminate mentioning first and last indexes


def quick_sort_helper(my_list, left, right):
   # check if there is more than one element in the sublist to be sorted
    if left < right:
      #  choose a pivot element and partition the list into two sublists
        pivot_index = pivot(my_list, left, right)
      #   recursively sort the left sublist(elements less than pivot)
        quick_sort_helper(my_list, left, pivot_index - 1)
      #   recursively sort the right sublist(elements greater than or equal to pivot)
        quick_sort_helper(my_list, pivot_index + 1, right)
   #  when there is only element or on elements left to be sorted, return the sorted list
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))

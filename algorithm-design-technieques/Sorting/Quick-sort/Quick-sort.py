# Quick sort algorithm 

# Quicksort is an efficient sorting algorithm.
# The quicksort algorithm is based on the divide-and-conquer class of algorithms,
# similar to the merge sort algorithm,
# it works better compared to the other sorting algorithms (O(n^2))
# quick-sorting is partitioning a given list or list. 
# first select a pivot element(pivot point).(it's partitioning step)
def partition(unsorted_list, first_index, last_index):
   pivot = unsorted_list[first_index]
   pivot_index = first_index
   index_of_last_element = last_index
   less_than_pivot_index = index_of_last_element
   greater_than_pivot_index = first_index + 1
   while True:
      while unsorted_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
         greater_than_pivot_index += 1
      while unsorted_list[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
         less_than_pivot_index -= 1
      if greater_than_pivot_index < less_than_pivot_index:
         temp = unsorted_list[greater_than_pivot_index]
         unsorted_list[greater_than_pivot_index] = unsorted_list[less_than_pivot_index]
         unsorted_list[less_than_pivot_index] = temp
      else:
         break
   unsorted_list[pivot_index] = unsorted_list[less_than_pivot_index]
   unsorted_list[less_than_pivot_index] = pivot
   return less_than_pivot_index
         
def quick_sort(unsorted_list, first, last):
   if last - first <= 0:
      return 
   else:
      partition_point = partition(unsorted_list, first, last)
      quick_sort(unsorted_list, first, partition_point - 1)
      quick_sort(unsorted_list, partition_point + 1, last)
      
my_list = [43, 3, 77, 89, 4, 20]
print(my_list)
quick_sort(my_list, 0, 5)
print(my_list)
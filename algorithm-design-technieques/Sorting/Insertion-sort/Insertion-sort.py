# Insertion sort algorithm
# insertion sort is that we maintain two sublists,
# one that is sorted and one that is not sorted
# it requires N iterations to sort the entire list
# a worst-case runtime complexity of O(n^2)
def insertion_sort(unsorted_list):
   for index in range(1, len(unsorted_list)):
      search_index = index
      insert_value = unsorted_list[index]
      while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
         unsorted_list[search_index] = unsorted_list[search_index - 1]
         search_index -= 1 
      unsorted_list[search_index] = insert_value
   
my_list = [5, 1, 100, 2, 10]
print("Original list", my_list)
insertion_sort(my_list)
print("Sorted list", my_list)
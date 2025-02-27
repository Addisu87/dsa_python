# Sorting means arranging all the items in a list in ascending or descending order.

#  Bubble-sort:- swap the adjacent items if they are not in the correct order
#  a worst-case runtime complexity of O(n^2) - it is not efficient
def bubble_sort(unordered_list):
   iteration_number = len(unordered_list) - 1
   for i in range(iteration_number, 0, -1):
      for j in range(i):
         if unordered_list[j] > unordered_list[j + 1]:
            temp = unordered_list[j]
            unordered_list[j] = unordered_list[j + 1]
            unordered_list[j + 1] = temp 

my_list = [4, 3, 2, 1]
bubble_sort(my_list)
print(my_list)

my_list = [1, 12, 3, 4]
bubble_sort(my_list)
print(my_list)
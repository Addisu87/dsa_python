# Unordered linear search
# unordered linear search has a worst-case running time of O(n)
# if the list is short and unsorted, then it is suitable

def search(unordered_list, term):
   for i, item in enumerate(unordered_list):
      if term == unordered_list[i]:
         return i
   return None


list1 = [60, 1, 88, 10, 11, 600]

search_term = 10
index_position = search(list1, search_term)
print(index_position)

list2 = ['packt', 'publish', 'data']

search_term2 = 'data'
Index_position2 = search(list2, search_term2)
print(Index_position2)
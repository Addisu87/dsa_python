
# binary search algorithm is based on the divide-and-conquer design technique

def binary_search(arr, start, end, key):
  while start <= end: 
    mid = start + (end - start)//2
    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      start = mid + 1
    else:
      end = mid - 1
      
  return -1

# Example search a specific value
arr = [4, 6, 9, 13, 14, 21, 24, 38]
x = 13
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)
# merge sort is using divide and conquer algorithm technique

# recursively divides the list
def merge_sort(unsorted_list):
    # Base case
    if len(unsorted_list) == 1:
        return unsorted_list

    mid_point = int(len(unsorted_list)//2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
 
    return merge(half_a, half_b)

# to combine the results


def merge(first_sublist, second_sublist):
    i = j = 0
    merge_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merge_list.append(first_sublist[i])
            i += 1
        else:
            merge_list.append(second_sublist[j])
            j += 1

    while i < len(first_sublist):
        merge_list.append(first_sublist[i])
        i += 1

    while j < len(second_sublist):
        merge_list.append(second_sublist[j])
        j += 1

    return merge_list


# example sort this
ads = [12, 61, 16, 14, 18, 11, 41]
print(merge_sort(ads))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array


arr = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

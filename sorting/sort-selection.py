def selectionSorting(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print(arr)
    return arr


a = [0, 8, 34, 3, 10, 9, 20, 32, 34]
selectionSorting(a)
b = [0, 1, 5, 2, 3, 4, 6, 7,  10, 8, 9]
selectionSorting(b)
c = [1]
selectionSorting(c)

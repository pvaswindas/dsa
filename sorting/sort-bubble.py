def bubbleSort(arr):
    size = len(arr)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    print(arr)
    return


a = [1, 8, 5, 2, 6, 19, 11, 40, 34, 10]
bubbleSort(a)

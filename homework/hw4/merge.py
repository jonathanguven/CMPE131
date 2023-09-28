def merge_list(list1, list2):
    result = list1 + list2

    def heapify(arr, N, i):
        largest = i  
        l = 2 * i + 1   
        r = 2 * i + 2  
        if l < N and arr[largest] < arr[l]:
            largest = l
        if r < N and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            heapify(arr, N, largest)

    def heapSort(arr):
        N = len(arr)
        for i in range(N//2 - 1, -1, -1):
            heapify(arr, N, i)
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] 
            heapify(arr, i, 0)
    
    heapSort(result)
    return result

print(merge_list([1, 5, 3, 7], [6, 2, 4]))
print(merge_list([1, 5, 3, 2], [2, 1, 4, 5, 6]))
print(merge_list([1, 5, 9], []))
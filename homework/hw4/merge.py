def merge_list(list1, list2):
    result = list1 + list2

    def sort(array):
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min]:
                    min = j
            (array[i], array[min]) = (array[min], array[i])
        
    sort(result)
    return result

print(merge_list([1, 5, 3, 7], [6, 2, 4]))
print(merge_list([1, 5, 3, 2], [2, 1, 4, 5, 6]))
print(merge_list([1, 5, 9], []))
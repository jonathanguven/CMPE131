def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "invalid input"
    for num in list1 + list2:
        if not isinstance(num, int):
            return "all list elements must be integers"

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
print(merge_list([1, 5, 3, 2], 3))
print(merge_list([1, 5, 9], ["hello", "world"]))
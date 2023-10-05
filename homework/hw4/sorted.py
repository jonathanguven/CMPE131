def sort_dictionary(dictionary):
    if not isinstance(dictionary, dict):
        return "input is not a valid dictionary"
    sorted(dictionary.keys(), reverse=True)
    return [(name, dictionary[name][0]) for name in dictionary]

print(sort_dictionary({'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}))
print(sort_dictionary(23))
print(sort_dictionary([1, 2, 3, 4, 5]))

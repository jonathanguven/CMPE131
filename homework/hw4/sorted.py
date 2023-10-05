def sort_dictionary(dict):
    sorted(dict.keys(), reverse=True)
    return [(name, dict[name][0]) for name in dict]

print(sort_dictionary({'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}))
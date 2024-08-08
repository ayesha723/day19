def reverse_and_sort_dict(d):
    # Use list comprehension to create a list of tuples with values and keys reversed
    reversed_tuples = [(value, key) for key, value in d.items()]
    
    # Sort the list of tuples by the value (which is now the first element of each tuple)
    sorted_reversed_tuples = sorted(reversed_tuples)
    
    return sorted_reversed_tuples

# Example usage
example_dict = {'a': 10, 'b': 1, 'c': 22}
result = reverse_and_sort_dict(example_dict)
print(result)

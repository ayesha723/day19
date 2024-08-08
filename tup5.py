# Original tuple
my_tuple = (1, 2, 3, 4, 5)

def swap():
    # Define indices to swap
    index1, index2 = 1, 2

    # Create a new tuple with swapped elements
    temp_list = list(my_tuple)  # Convert tuple to list
    temp_list[index1], temp_list[index2] = temp_list[index2], temp_list[index1]  # Swap elements
    new_tuple = tuple(temp_list)  # Convert list back to tuple
    
    return new_tuple

# Call the function and print the result
swapped_tuple = swap()
print(swapped_tuple)

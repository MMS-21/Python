"""This script sorts a dictionary by its values in ascending order"""
# Create a dictionary with key-value pairs
dictionary_to_be_sorted = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sort the dictionary by values using a lambda function as the key argument
sorted_dict = dict(sorted(dictionary_to_be_sorted.items(), key=lambda item: item[1]))

# Print the sorted dictionary
print(sorted_dict)
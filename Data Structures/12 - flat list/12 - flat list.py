"""This script creates a flat list from a nested list"""
# Create an empty list to store the flattened elements
flat_list = []

# Defining the nested list to be flattened
nested_list = [1, [2, [3, 4], 5], [6, 7], 8,[6, 7, 1],["c", "b", "a"]]

# Creating a copy of the nested list to avoid modifying the original
stack = nested_list[:]

# Iterate while the stack is not empty
while stack:
  # Remove the first element from the stack
  item = stack.pop(0)

  # If the item is a list, add its elements to the beginning of the stack
  if isinstance(item, list):
    stack = item + stack

  # If the item is not a list, add it to the flattened list
  else:
    flat_list.append(item)

# Print the flattened list
print(flat_list)
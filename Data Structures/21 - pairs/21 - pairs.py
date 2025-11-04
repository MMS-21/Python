""" Module to generate all unique pairs of numbers from a list. """
# Defining a list of numbers
numbers_list = [0,1,2,3,4,5]

# Create a list of pairs using a list comprehension
pairs = [[i, j] for i in numbers_list for j in numbers_list if i <= j]
print(pairs)
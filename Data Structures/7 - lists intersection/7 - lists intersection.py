"""This script finds the intersection of two lists and prints the common elements"""
# Example list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert both lists to sets and find the intersection
intersection = set(list1) & set(list2)

# printing the results
print(intersection)
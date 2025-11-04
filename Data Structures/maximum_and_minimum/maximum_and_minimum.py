"""This script finds the maximum and minimum values in a list of numbers"""
# A list of numbers
numbers = [1, 5, 3, 9, 2]
# Initialize max_value and min_value to the first element in the list
max_value = numbers[0]
min_value = numbers[0]

# iterating through the numbers list
for num in numbers:
    # comparing between numbers to get the max and min values
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Printing the final values
print("Maximum value:", max_value)
print("Minimum value:", min_value)
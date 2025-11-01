"""This script filters even numbers from a list of numbers"""
# a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# using list comprehension to get only even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
# Printing the even numbers
print(even_numbers)     
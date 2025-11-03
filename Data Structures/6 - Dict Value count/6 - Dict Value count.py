"""This script counts the frequency of each character in a given string"""
#This module implements specialized container datatypes providing
#alternatives to Python's general purpose built-in containers, dict,
#list, set, and tuple.
from collections import Counter

def char_frequency(example_string):
    # Using Counter to count the frequency of each character in the string
    frequency_dict = dict(Counter(example_string))
    
    # Return the dictionary with character frequencies
    return frequency_dict

# Example string
example_string = "hello to python's world"
final_count = char_frequency(example_string)

print(final_count)

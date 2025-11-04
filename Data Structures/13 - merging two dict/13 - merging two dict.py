"""Merging two dictionaries in Python."""
def merging_dictionaries(dict1, dict2):
  """Merges two dictionaries, adding values for keys that appear in both.

  Args:
    dict1: The first dictionary.
    dict2: The second dictionary.

  Returns:
    A new dictionary containing the merged elements of both dictionaries.
  """
  # Merge Operator (|)  
  merged_dict = dict1 | dict2
  return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(merging_dictionaries(dict1, dict2))
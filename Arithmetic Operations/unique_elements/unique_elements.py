""" A program to check if all elements in a list are unique. """
def unique_elements(lst):
    # Check if the length of the list is equal to the length of the set 
    # the idea of using the set is that the set removes duplicates
    # So if the len of a lst is equal to it self converted to a set
    # Means that it does have unique values
    return len(lst) == len(set(lst))

# Example of a list that has unique values
a_list = [1, 2, 3, 4, 5]
# Printing the result
print(unique_elements(a_list))  

# Example of a list that does not have unique values
a_list_with_duplicates = [1, 2, 3, 4, 5, 1]
# Printing the result
print(unique_elements(a_list_with_duplicates))  
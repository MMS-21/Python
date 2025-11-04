"""
    Perform a binary search to find the index of a target element in a sorted list.
"""

def binary_search(sorted_list, target):
    """
    Perform a binary search to find the index of a target element in a sorted list.

    Args:
        sorted_list: A list of sorted elements.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    # Initialize left and right pointers
    left, right = 0, len(sorted_list) - 1  
    # Continue searching while there are elements to inspect
    while left <= right:  
        # Find the middle index
        mid = (left + right) // 2  
         # Check if the middle element is the target
        if sorted_list[mid] == target: 
            # Return the index if found
            return mid  
        # If target is greater, ignore the left half
        elif sorted_list[mid] < target:  
            left = mid + 1
         # If target is smaller, ignore the right half
        else: 
            right = mid - 1
     # Return -1 if the target is not found
    return -1 


if __name__ == "__main__":
    # Example sorted list
    sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    # The number we want to search for
    target_number = 8  

    # Call the binary_search function
    result = binary_search(sorted_numbers, target_number)

    # Output the result
    if result != -1:
        print(f"Element {target_number} found at index: {result}")
    else:
        print(f"Element {target_number} not found in the list.")

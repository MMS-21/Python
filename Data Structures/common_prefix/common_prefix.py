"""  Module to find the longest common prefix among a list of strings."""
def longest_common_prefix(strs):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix string.
    """
    # If the list is empty, return an empty string
    if not strs:  
        return ""

    # Start with the first string as the initial prefix
    prefix = strs[0]

    # Compare the prefix with each string in the list
    for string in strs[1:]:
        # Continue to reduce the prefix until it matches the start of the current string
        while not string.startswith(prefix):
            # Remove the last character from prefix
            prefix = prefix[:-1]  
            # If prefix is empty, return an empty string
            if not prefix:  
                return ""
    # Return the longest common prefix
    return prefix  

if __name__ == "__main__":
    # Example list of strings
    strings = ["flower", "flow", "flight"]  
    # Find the longest common prefix
    result = longest_common_prefix(strings)  
    print(f"The longest common prefix is: '{result}'")

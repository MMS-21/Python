""" Module to generate all possible subsets of a given set. """
def generate_subsets(set_to_generate):

    # Initialize the list to hold all subsets
    subsets = []
    
    # Start with the empty subset
    subsets.append([])

    # Iterate through each element in the provided set
    for element in set_to_generate:
        # For each existing subset, create a new subset that includes the current element
        new_subsets = [subset + [element] for subset in subsets]
        
        # Extend the existing list of subsets with the newly created subsets
        subsets.extend(new_subsets)

    # Return the list containing all possible subsets
    return subsets


# Define the set to generate subsets from
set_to_generate = {1, 2, 3, 4}
# Call the function to generate subsets 
subsets = generate_subsets(set_to_generate)
# Print the resulting subsets  
print(subsets)  

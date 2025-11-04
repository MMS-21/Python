# Function to sum the values of a tuple
def tuple_elements_summation(number_tuple):
    """
    Calculates the sum of all elements in a tuple.

    :param number_tuple: Tuple of numbers to sum
    :return: Sum of the elements
    """
    # Initialize the sum to zero
    total = 0
    # Traverse each element in the tuple  
    for number in number_tuple:  
        # Add each number to the total
        total += number  
    # Return the final sum
    return total  

 # Tuple of numbers
numbers = (1, 17, 5, 4, 5) 


if __name__ == "__main__":
    print(f"The Tuple is {numbers}")
    print(f"The Summation Of Tuple Values: {tuple_elements_summation(numbers)}")
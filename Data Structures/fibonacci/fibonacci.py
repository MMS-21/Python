"""This module defines a function to compute Fibonacci numbers recursively."""

def fibonacci(n):
    """Returns the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    # Base case: the first two Fibonacci numbers
    # Fibonacci(0) is 0
    if n <= 0:
        return 0
    # Fibonacci(1) is 1  
    elif n == 1:
        return 1  
    else:
        # Recursive case: sum of the two previous Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# A list of test numbers    
numbers = [1,2,4,5,6,7]

# loop through the list
for n in numbers: 
    # results aquiring
    result = fibonacci(n)
    # printing the results out
    print(f"The {n}th Fibonacci number is: {result}")
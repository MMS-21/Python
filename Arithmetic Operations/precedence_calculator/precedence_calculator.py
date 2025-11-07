""" A simple precedence calculator that evaluates arithmetic expressions
    while respecting operator precedence. """

def precedence_calculator():
    """Calculates arithmetic expressions with operator precedence.

    Args:
        expression (str): The arithmetic expression to evaluate.

    Returns:
        float: The result of the calculation.

    Raises:
        SyntaxError: If the expression is syntactically incorrect.
        ValueError: If the expression contains invalid characters or operations.
        ZeroDivisionError: If the expression involves division by zero.
        TypeError: If the expression contains incompatible data types.
    """
    # Reading the arithmatic expression from The STDN and storing it a variable
    arithmetic_expression = input("Enter an arithmetic expression: ")
    try:
        # solving the arithmetic expression and storing the result in a variable
        result = eval(arithmetic_expression)
        # Printing the results
        print(f"The result is: {result}")
    # Handling any Errors that may appear 
    except (SyntaxError, ValueError, ZeroDivisionError, TypeError) as e:
        # Printing a message with the type of Error
        print(f"Error: {e}") 

if __name__ == "__main__":
    # Calling the Function to
    precedence_calculator()


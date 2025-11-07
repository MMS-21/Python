""" This script performs basic calculations using functions. """

# Summation Function        
def add(x, y):
    # Summation Operation
    return x + y

# Subtraction Function
def subtract(x, y):
    # Subtraction Operation
    return x - y

# Multiplication Function
def multiply(x, y):
    # Multiplication Operation
    return x * y

# Division Function 
def divide(x, y):
    # Division Operation
    return x / y

# Calculator Function 
def basic_calculator():
    # Reading the first value from the STDIN
    x = float(input("Enter the first number: "))
    # Reading the Second value from the STDIN
    y = float(input("Enter the second number: "))
    # The kind of operations that required to be performed
    operation = input("Choose operation (+, -, *, /): ")
    
    # Handling the operations Required
    # Using if statement
    # The Adding Operation
    if operation == '+':
        print(f"The result is: {add(x, y)}")
    # The Subtraction Operation
    elif operation == '-':
        print(f"The result is: {subtract(x, y)}")
    # The Multiplication Operation
    elif operation == '*':
        print(f"The result is: {multiply(x, y)}")
    # The Division Operation
    elif operation == '/':
        # Handling the zero division error
        if y != 0:
            print(f"The result is: {divide(x, y)}")
        # Printing the Error Message
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")


if __name__ == "__main__":
    # Calling the Function to Conduct the operations 
    basic_calculator()
"""This script demonstrates how the order of operations affects the result of arithmetic expressions in Python."""
# Function explains how the precedence of parentheses affects the result value
def order_of_operations():
    # Example Operations
    example1 = (5 + 3) * 2
    example2 = 5 + (3 * 2)
    # Printing the results of each example
    print(f"Example 1: (5 + 3) * 2 = {example1}")
    print(f"Example 2: 5 + (3 * 2) = {example2}")



if __name__ == "__main__":
    # Calling the function
    order_of_operations()
    # Explanation message
    print("This is how changing the parentheses affects the result!")
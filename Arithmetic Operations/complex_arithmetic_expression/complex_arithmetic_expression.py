"""This script reads a complex arithmetic expression from the user,
evaluates it, and prints the result along with an explanation of how Python handles operator precedence."""
# Reading the Mathematical Expression from the STDIN
expression = input("Enter a complex arithmetic expression: ")
# Conducting the Mathematical operation and storing the value in a result variable to use it later
result = eval(expression)
# Print ing the result
print(f"The result of the expression '{expression}' is {result}")
# Printingthe explanation of how python solve the mathematical operations
print(""" Explanation:
            Python uses operator precedence: PEMDAS 
            (Parentheses, Exponentiation, Multiplication, Division, Addition, Subtraction).""")

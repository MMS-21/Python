""" Module to evaluate postfix expressions using a stack. """
# Function to evaluate a postfix expression using a stack
def evaluate_postfix(expression):
    # Initialize an empty stack
    stack = []  

    # Iterate through each character in the expression
    for char in expression:
        # If the character is a digit
        if char.isdigit():  
            # Push it onto the stack
            stack.append(int(char))  
        # If the character is an operator
        else:  
            # Pop the top two elements from the stack
            b = stack.pop()  
            a = stack.pop()

            # Perform the operation based on the operator
            if char == '+':
                 # Add
                stack.append(a + b) 
            elif char == '-':
                # Subtract
                stack.append(a - b)  
            elif char == '*':
                # Multiply
                stack.append(a * b)  
            elif char == '/':
                # Divide
                stack.append(a / b)  

    # The final result will be the only element in the stack
    return stack[0]  

# Example usage
postfix_expression = "25*34*+"  
result = evaluate_postfix(postfix_expression)  
print(result) 

"""This script implements a simple stack data structure with push and pop operations"""
class Stack:
    # Initialize an empty list to represent the stack
    def __init__(self):
        self.stack = []
    # Add item to the top of the stack
    def push(self, item):
        self.stack.append(item)
    
    # Remove and return the top item
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  
        else:
            return "Stack is empty"
      # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)

print(my_stack.pop()) 
print(my_stack.pop()) 
print(my_stack.pop()) 


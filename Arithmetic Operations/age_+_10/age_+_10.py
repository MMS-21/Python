""" This program reads a user's name and age from standard input (STDIN) and then prints a message indicating how old the user will be in 10 years. """
#  Reading The name from STDIN
name = input("Enter your name: ")
# Reading The age from STDIN
age = int(input("Enter your age: "))
# Printing the name and age plus 10 years
print(f"Hello, {name}. You will be {age + 10} years old in 10 years.")

"""A program to demonstrate bitwise operations: AND, OR, XOR, and NOT."""
def bitwise_operations(num1, num2):
  """Performs bitwise AND, OR, XOR, and NOT operations on two integers.

  Args:
    num1: The first integer.
    num2: The second integer.
  """

  # Bitwise AND
  and_result = num1 & num2
  print(f"Bitwise AND: {num1} & {num2} = {and_result}")

  # Bitwise OR
  or_result = num1 | num2
  print(f"Bitwise OR: {num1} | {num2} = {or_result}")

  # Bitwise XOR
  xor_result = num1 ^ num2
  print(f"Bitwise XOR: {num1} ^ {num2} = {xor_result}")

  # Bitwise NOT (applied to num1)
  not_result = ~num1
  print(f"Bitwise NOT: ~{num1} = {not_result}")

# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the bitwise_operations function
bitwise_operations(num1, num2)
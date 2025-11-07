"""A program to swap two numbers using the XOR bitwise operator."""
def swap_numbers(x, y):
  """Swaps two numbers using the XOR bitwise operator.

  Args:
    x: The first number.
    y: The second number.

  Returns:
    None. The numbers are swapped in place.
  """

  # Perform XOR operations to swap the values
  # in the first line of code calculates the XOR of x and y and stores the result in x. 
  # In essence, it combines the unique bits from both x and y
  x = x ^ y
  # This line calculates the XOR of the new x (which contains the combined unique bits) and the original y.
  y = x ^ y
  # This line calculates the XOR of the new x (which contains the combined unique bits) and
  # the original y (which now holds the original value of x).
  x = x ^ y

  # Print the swapped values
  print("Swapped values:")
  print("x =", x)
  print("y =", y)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the swap_numbers function
swap_numbers(num1, num2)
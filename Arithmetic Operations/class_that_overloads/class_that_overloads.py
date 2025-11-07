""" A program to demonstrate complex number subtraction using operator overloading. """
# Class For complex number
class Complex:
  """Represents a complex number.

  Attributes:
    real: The real part of the complex number.
    imaginary: The imaginary part of the complex number.
  """

  def __init__(self, real, imaginary):
    """Initializes a new Complex object.

    Args:
      real: The real part of the complex number.
      imaginary: The imaginary part of the complex number.
    """
    self.real = real
    self.imaginary = imaginary

  def __sub__(self, other):
    """Subtracts another complex number from this complex number.

    Args:
      other: The other complex number to subtract.

    Returns:
      A new Complex object representing the difference of the two complex numbers.
    """
    return Complex(self.real - other.real, self.imaginary - other.imaginary)

  def __str__(self):
    """Returns a string representation of the complex number.

    Returns:
      A string representation of the complex number in the format "(real + imaginaryi)".
    """
    return f"({self.real} + {self.imaginary}i)"

def complex_subtraction():
  """Demonstrates complex number subtraction.

  This function creates two Complex objects, subtracts them, and prints the result.
  """
  c1 = Complex(4, 3)
  c2 = Complex(2, 1)
  result = c1 - c2
  print(f"Result of complex number subtraction: {result}")

# Calling  the complex_subtraction function to demonstrate complex number subtraction
complex_subtraction()
""" A program to perform vector addition in 2D space. """
class Vector:
  """Represents a 2D vector.

  Attributes:
    x: The x-coordinate of the vector.
    y: The y-coordinate of the vector.
  """

  def __init__(self, x, y):
    """Initializes a new Vector object.

    Args:
      x: The x-coordinate of the vector.
      y: The y-coordinate of the vector.
    """
    self.x = x
    self.y = y

  def __add__(self, other):
    """Adds two vectors together.

    Args:
      other: The other vector to add.

    Returns:
      A new Vector object representing the sum of the two vectors.
    """
    return Vector(self.x + other.x, self.y + other.y)

  def __str__(self):
    """Returns a string representation of the vector.

    Returns:
      A string representation of the vector in the format "Vector(x, y)".
    """
    return f"Vector({self.x}, {self.y})"

def vector_addition():
  """Demonstrates vector addition.

  This function creates two Vector objects, adds them together, and prints the result.
  """
  v1 = Vector(1, 2)
  v2 = Vector(3, 4)
  v3 = v1 + v2
  print(f"Result of vector addition: {v3}")

# Calling the vector_addition function to demonstrate vector addition
vector_addition()

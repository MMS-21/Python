""" A program to perform matrix multiplication. """
class Matrix:
  """Represents a matrix.

  Attributes:
    matrix: A list of lists representing the matrix.
  """

  def __init__(self, matrix):
    """Initializes a new Matrix object.

    Args:
      matrix: A list of lists representing the matrix.
    """
    self.matrix = matrix

  def __mul__(self, other):
    """Multiplies two matrices together.

    Args:
      other: The other matrix to multiply.

    Returns:
      A new Matrix object representing the product of the two matrices.
    """
    result = []
    for i in range(len(self.matrix)):
      row = []
      for j in range(len(other.matrix[0])):
        total = 0
        for k in range(len(other.matrix)):
          total += self.matrix[i][k] * other.matrix[k][j]
        row.append(total)
      result.append(row)
    return Matrix(result)

  def __str__(self):
    """Returns a string representation of the matrix.

    Returns:
      A string representation of the matrix.
    """
    # the Following expression takes a list of lists (the self.matrix attribute) and 
    # returns a new list where each element is 
    # a string representation of a row from the original list.
    return "\n".join([str(row) for row in self.matrix])

def matrix_multiplication():
  """Demonstrates matrix multiplication.

  This function creates two Matrix objects, multiplies them together, and prints the result.
  """
  m1 = Matrix([[5, 2], [8, 4]])
  m2 = Matrix([[5, 6], [7, 9]])
  # The multiplication Operation
  result = m1 * m2
  print(f"Matrix multiplication result:\n{result}")

matrix_multiplication()
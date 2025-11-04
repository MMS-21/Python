""" Module to rotate a matrix 90 degrees clockwise. """
def rotate_matrix(matrix):
    # Getting the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Creating a new matrix to hold the rotated result
    # Creating a cols x rows matrix
    rotated = [[0] * rows for _ in range(cols)]  
    
    # Filling the new matrix with rotated values
    for i in range(rows):
        for j in range(cols):
            # Placing elements in the new positions
            rotated[j][rows - 1 - i] = matrix[i][j]  

    return rotated


original_matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Rotate the matrix
rotated_matrix = rotate_matrix(original_matrix)  
print("Original Matrix:")
for row in original_matrix:
    print(row)
print("\nRotated Matrix:")
for row in rotated_matrix:
    print(row)
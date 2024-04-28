def vertical_order_traversal(matrix):
    if not matrix:
        return []

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Traverse each column - first Notice the pattern 
    for col in range(cols):
        # Traverse each row in the current column
        for row in range(rows):
            print(matrix[row][col], end=" ")

        print()  # Print newline after each column

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vertical_order_traversal(matrix)

1 4 7 
2 5 8 
3 6 9 


vertical reverse order traversal 
def vertical_order_traversal(matrix):
    if not matrix:
        return []

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Traverse each column - first Notice the pattern 
    for col in reversed(range(cols)):
        # Traverse each row in the current column
        for row in range(rows):
            print(matrix[row][col], end=" ")

        print()  # Print newline after each column

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vertical_order_traversal(matrix)

output :
7 4 1 
8 5 2 
9 6 3 

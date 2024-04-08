array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get the dimensions of the array
num_rows = len(array_2d)
num_cols = len(array_2d[0])  # Assuming all rows have the same length

# Traverse the array in reverse order (bottom-up)
for i in range(num_rows - 1, -1, -1):  # Start from the last row and go backwards
    for j in range(num_cols - 1, -1, -1):  # Start from the last column and go backwards
        print(array_2d[i][j], end=' ')
    print()  # Print a newline after each row

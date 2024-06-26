array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Note: row remains constant but column decrements backwards thats how the for loop designed. 

# Get the dimensions of the array
num_rows = len(array_2d)
num_cols = len(array_2d[0])  # Assuming all rows have the same length

# Traverse the array in reverse order (bottom-up)
for i in range(num_rows):  # Start from the 0th row .
    for j in range(num_cols - 1, -1, -1):  # Start from the last column and go backwards
        print(array_2d[i][j], end=' ')
    print()  # Print a newline after each row

Result 
#######
3 2 1 
6 5 4 
9 8 7 



#row-wise reverse traversal (bottom-up)
#Notice rows and columns both decrements thats how for loop designed to pick the elements
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

Result 
####
9 8 7 
6 5 4 
3 2 1







def sink_island(r: int, c: int, grid: List[List[int]]) -> List[List[int]]:
    grid[r][c] = 0

    for delta_row, delta_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row = r + delta_row
        neighbor_column = c + delta_column
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_column < len(grid[0]):
            if grid[neighbor_row][neighbor_column] == 1:
                sink_island(neighbor_row, neighbor_column, grid)

    return grid


def count_number_of_islands(grid: List[List[int]]) -> int:
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                sink_island(r, c, grid)
                res += 1
    return res  

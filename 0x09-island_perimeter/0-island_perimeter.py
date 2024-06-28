#!/usr/bin/python3
""" Calculates the perimeter of an island. """


def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.

    Args:
    grid: A list of lists of integers, where 0 represents water
    and 1 represents land.

    Returns:
      The perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 for each land cell
                if row > 0 and grid[row - 1][col] == 1:  # Check north neighbor
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check west neighbor
                    perimeter -= 2
    return perimeter

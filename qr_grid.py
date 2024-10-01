import numpy as np

def initialize_qr_grid(version=1):
    # Version 1 is 21x21 pixels
    size = 21
    grid = np.zeros((size, size), dtype=int)

    # Add finder patterns
    add_finder_pattern(grid, 0, 0)
    add_finder_pattern(grid, 0, size - 7)
    add_finder_pattern(grid, size - 7, 0)
    
    # Add timing patterns
    add_timing_patterns(grid)

    return grid

def add_finder_pattern(grid, row, col):
    pattern = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    
    for i in range(7):
        for j in range(7):
            grid[row + i, col + j] = pattern[i][j]

def add_timing_patterns(grid):
    size = grid.shape[0]
    for i in range(8, size - 8):
        grid[6, i] = i % 2  # Horizontal timing pattern
        grid[i, 6] = i % 2  # Vertical timing pattern

def is_reserved_area(row, col, size):
    # Skip finder patterns and timing pattern areas
    if (row < 7 and col < 7) or (row < 7 and col >= size - 7) or (row >= size - 7 and col < 7):
        return True  # Inside finder patterns
    if row == 6 or col == 6:
        return True  # Inside timing patterns
    return False

def place_data_in_grid(grid, bit_string):
    size = grid.shape[0]
    row = size - 1
    col = size - 1
    bit_index = 0
    direction_up = True  # Flag to alternate between up and down

    while col > 0 and bit_index < len(bit_string):
        if col == 6:  # Skip vertical timing pattern
            col -= 1

        if direction_up:
            for r in range(size - 1, -1, -1):  # Move upward
                if bit_index >= len(bit_string):
                    break
                if not is_reserved_area(r, col, size) and grid[r, col] == 0:  # Skip reserved areas
                    grid[r, col] = int(bit_string[bit_index])
                    bit_index += 1
                if col > 0 and not is_reserved_area(r, col - 1, size) and grid[r, col - 1] == 0:
                    grid[r, col - 1] = int(bit_string[bit_index])
                    bit_index += 1
            direction_up = False  # Change direction after reaching top
        else:
            for r in range(size):  # Move downward
                if bit_index >= len(bit_string):
                    break
                if not is_reserved_area(r, col, size) and grid[r, col] == 0:
                    grid[r, col] = int(bit_string[bit_index])
                    bit_index += 1
                if col > 0 and not is_reserved_area(r, col - 1, size) and grid[r, col - 1] == 0:
                    grid[r, col - 1] = int(bit_string[bit_index])
                    bit_index += 1
            direction_up = True  # Change direction after reaching bottom

        col -= 2  # Move two columns to the left

    return grid

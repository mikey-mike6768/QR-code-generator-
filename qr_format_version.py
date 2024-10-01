import numpy as np
from qr_grid import initialize_qr_grid  # Import the grid initialization function

def add_format_info(grid, format_info="11101100"):
    # Placeholder function to add format info (simplified)
    grid[0, 0:8] = list(map(int, format_info[:8]))  # Add to top-left finder pattern area
    return grid

# Initialize the QR grid
qr_grid = initialize_qr_grid()  # Initialize the grid with default version 4

# Add format information
qr_grid = add_format_info(qr_grid)

# Print the updated grid
print(qr_grid)

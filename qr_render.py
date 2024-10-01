from PIL import Image, ImageDraw
from qr_grid import initialize_qr_grid, place_data_in_grid  # Import the updated functions
from qr_data_encoding import encode_alphanumeric  # Import the encoding function
from qr_error_correction import apply_error_correction  # Import error correction

def render_qr(grid, scale=10, color=(0, 0, 0), bg_color=(255, 255, 255), logo_path=None):
    size = grid.shape[0]
    img = Image.new("RGB", (size * scale, size * scale), bg_color)
    draw = ImageDraw.Draw(img)

    for i in range(size):
        for j in range(size):
            if grid[i, j] == 1:
                draw.rectangle(
                    [(j * scale, i * scale), ((j + 1) * scale - 1, (i + 1) * scale - 1)], 
                    fill=color
                )

     # Add logo in the center if provided
    if logo_path:
        logo = Image.open(logo_path)
        logo_size = int(size * scale / 4)
        logo = logo.resize((logo_size, logo_size))
        logo_position = ((size * scale - logo_size) // 2, (size * scale - logo_size) // 2)
        img.paste(logo, logo_position, logo)

    img.show()  # Display or use img.save('qr_code.png') to save it

# Initialize the QR grid
qr_grid = initialize_qr_grid()

# Encode the data and apply error correction
data = "HELLO QR CODE THIS IS A LONGER STRING TO FILL THE QR CODE BETTER"
encoded_data = encode_alphanumeric(data)
encoded_data_with_correction = apply_error_correction(encoded_data)

# Place the data in the grid
qr_grid = place_data_in_grid(qr_grid, encoded_data_with_correction)

# Render the QR code with custom color, background, and optional logo
render_qr(qr_grid, scale=10, color=(0, 0, 0), bg_color=(255, 255, 255), logo_path=None)

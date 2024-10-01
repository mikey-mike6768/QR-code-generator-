from qr_data_encoding import encode_alphanumeric  # Correct function import
from reedsolo import RSCodec  # External library needed

def apply_error_correction(data_bits):
    # Apply Reed-Solomon error correction to the data bits
    rsc = RSCodec(10)  # 10 bytes for error correction
    # Convert the data to bytes for the RS library
    data_bytes = int(data_bits, 2).to_bytes((len(data_bits) + 7) // 8, 'big')
    encoded_bytes = rsc.encode(data_bytes)
    # Convert back to a bit string
    encoded_bits = ''.join(f'{byte:08b}' for byte in encoded_bytes)
    return encoded_bits

# Example usage
if __name__ == "__main__":
    data = "HELLO QR CODE THIS IS A TEST"
    encoded_data = encode_alphanumeric(data)  # Using the correct encoding function
    encoded_data_with_correction = apply_error_correction(encoded_data)
    print(f"Encoded Data with Error Correction: {encoded_data_with_correction}")

def encode_alphanumeric(data):
    alphanumeric_table = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
        'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
        'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36,
        '$': 37, '%': 38, '*': 39, '+': 40, '-': 41, '.': 42, '/': 43, ':': 44
    }

    bit_string = ""
    i = 0
    while i < len(data):
        if i + 1 < len(data):
            pair_value = alphanumeric_table[data[i]] * 45 + alphanumeric_table[data[i + 1]]
            bit_string += format(pair_value, '011b')
            i += 2
        else:
            bit_string += format(alphanumeric_table[data[i]], '06b')
            i += 1

    return bit_string

# Test encoding with more data
if __name__ == "__main__":
    data = "HELLO QR CODE THIS IS A LONGER STRING"
    encoded_data = encode_alphanumeric(data)
    print(f"Encoded Data: {encoded_data}")


def detect_mode(data):
    if all(char.isdigit() for char in data):
        return "Numeric"
    elif all(char.isalnum() or char in ['$', '%', '*', '+', '-', '.', '/', ':', ' '] for char in data):
        return "Alphanumeric"
    elif all(ord(char) < 256 for char in data):
        return "Byte"
    else:
        return "Kanji"

# Tests
test_data = ["12345", "HELLO", "Hello World!", "漢字"]
for data in test_data:
    print(f"Data: {data} -> Mode: {detect_mode(data)}")

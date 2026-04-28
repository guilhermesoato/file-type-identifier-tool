# This module provides functionality to identify file types based on their magic numbers.
MAGIC_NUMBERS = {
    "PDF": b"\x25\x50\x44\x46",
    "JPG": b"\xFF\xD8\xFF",
    "PNG": b"\x89\x50\x4E\x47",
    "ZIP": b"\x50\x4B\x03\x04",
    "EXE": b"\x4D\x5A"
}

# This function reads the first few bytes of a file to determine its type based on magic numbers.
def read_file_header(file_path, num_bytes=8):
    with open(file_path, "rb") as f:
        return f.read(num_bytes)

# This function identifies the file type by comparing the header bytes with known magic numbers.
def identify_file_type(header_bytes):
    for file_type, magic in MAGIC_NUMBERS.items():
        if header_bytes.startswith(magic):
            return file_type
    return "Unknown"

import os

# This function extracts the file extension from the given file path.
def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower().replace(".", "")

# This function checks for mismatches between the real file type and the expected type based on the file extension.
def check_mismatch(real_type, extension):
    mapping = {
        "pdf": "PDF",
        "jpg": "JPG",
        "jpeg": "JPG",
        "png": "PNG",
        "zip": "ZIP",
        "exe": "EXE"
    }

    expected_type = mapping.get(extension)

    if expected_type is None:
        return "Unknown extension"
    elif expected_type != real_type:
        return "⚠️ POSSIBLE MISMATCH: Real type is {} but extension is {}".format(real_type, extension)
    else:
        return "✅ Compatible type"
    
def main():
    file_path = input("Type the archive path: ")

    try:
        header = read_file_header(file_path)
        real_type = identify_file_type(header)
        extension = get_file_extension(file_path)
        result = check_mismatch(real_type, extension)

        print("\n=== File Analysis ===")
        print(f"Extension: .{extension}")
        print(f"Real type detected: {real_type}")
        print(f"Header (hex): {header.hex()}")
        print(f"Result: {result}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error analyzing the file: {e}")

if __name__ == "__main__":
    main()
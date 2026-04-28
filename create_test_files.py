#!/usr/bin/env python3
"""
Script to create test files for the File Type Identifier tool.
This script generates both legitimate and disguised test files.
"""

import os

def create_test_files():
    """Create all test files with proper magic numbers."""
    
    # Get the test_files directory path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(script_dir, 'test_files')
    
    # Ensure test directory exists
    os.makedirs(test_dir, exist_ok=True)
    
    # Define magic numbers (hex bytes)
    magic_numbers = {
        'PDF': b'\x25\x50\x44\x46\x0D\x0A\x25\xE2',  # %PDF
        'PNG': b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',  # PNG signature
        'JPG': b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46',  # JPG/JPEG
        'ZIP': b'\x50\x4B\x03\x04\x14\x00\x00\x00',  # PK.. (ZIP)
        'EXE': b'\x4D\x5A\x90\x00\x03\x00\x00\x00',  # MZ (EXE)
    }
    
    # Legitimate files (magic number matches extension)
    legitimate_files = {
        'legitimate_file.pdf': magic_numbers['PDF'],
        'legitimate_image.png': magic_numbers['PNG'],
        'legitimate_photo.jpg': magic_numbers['JPG'],
        'legitimate_archive.zip': magic_numbers['ZIP'],
        'legitimate_program.exe': magic_numbers['EXE'],
    }
    
    # Disguised files (magic number does NOT match extension)
    disguised_files = {
        'disguised_exe_as_pdf.pdf': magic_numbers['EXE'],      # EXE with .pdf extension
        'disguised_zip_as_jpg.jpg': magic_numbers['ZIP'],      # ZIP with .jpg extension
        'disguised_png_as_zip.zip': magic_numbers['PNG'],      # PNG with .zip extension
        'disguised_jpg_as_exe.exe': magic_numbers['JPG'],      # JPG with .exe extension
        'disguised_pdf_as_png.png': magic_numbers['PDF'],      # PDF with .png extension
    }
    
    # Create legitimate files
    print("📝 Creating legitimate test files...")
    for filename, magic_bytes in legitimate_files.items():
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(magic_bytes)
        print(f"   ✅ Created: {filename}")
    
    # Create disguised files
    print("\n⚠️  Creating disguised test files...")
    for filename, magic_bytes in disguised_files.items():
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(magic_bytes)
        print(f"   ⚠️  Created: {filename}")
    
    print("\n" + "="*70)
    print("🎉 All test files created successfully!")
    print("="*70)
    print(f"\nTest files location: {test_dir}")
    print(f"\nTotal files created: {len(legitimate_files) + len(disguised_files)}")
    print("\nYou can now test the File Type Identifier tool with these files!")

if __name__ == '__main__':
    create_test_files()

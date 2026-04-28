# File Type Identifier - Test Files

This directory contains test files for the File Type Identifier tool. Files are organized into two categories:

## ✅ Legitimate Files (PASS Verification)

These files have the correct magic numbers matching their file extensions:

| Filename | Extension | Magic Number | Expected Result |
|----------|-----------|--------------|-----------------|
| legitimate_file.pdf | .pdf | 25 50 44 46 (%PDF) | ✅ Compatible type |
| legitimate_image.png | .png | 89 50 4E 47 | ✅ Compatible type |
| legitimate_photo.jpg | .jpg | FF D8 FF E0 | ✅ Compatible type |
| legitimate_archive.zip | .zip | 50 4B 03 04 (PK) | ✅ Compatible type |
| legitimate_program.exe | .exe | 4D 5A (MZ) | ✅ Compatible type |

## ⚠️ Disguised Files (FAIL Verification - Mismatches)

These files have magic numbers that DO NOT match their file extensions:

| Filename | Extension | Actual Type | Magic Number | Expected Result |
|----------|-----------|-------------|--------------|-----------------|
| disguised_exe_as_pdf.pdf | .pdf | EXE | 4D 5A (MZ) | ⚠️ POSSIBLE MISMATCH |
| disguised_zip_as_jpg.jpg | .jpg | ZIP | 50 4B 03 04 | ⚠️ POSSIBLE MISMATCH |
| disguised_png_as_zip.zip | .zip | PNG | 89 50 4E 47 | ⚠️ POSSIBLE MISMATCH |
| disguised_jpg_as_exe.exe | .exe | JPG | FF D8 FF E0 | ⚠️ POSSIBLE MISMATCH |
| disguised_pdf_as_png.png | .png | PDF | 25 50 44 46 | ⚠️ POSSIBLE MISMATCH |

## 🧪 How to Test

Run the File Type Identifier tool on these test files:

```bash
python file_type_identifier.py
```

Then enter the full path to any test file, for example:
- `C:\Users\...\file_type_identifier\test_files\legitimate_file.pdf`
- `C:\Users\...\file_type_identifier\test_files\disguised_exe_as_pdf.pdf`

## 📝 Notes

- All files are **completely safe** - they contain only magic number signatures
- Files are small and won't affect your system
- These are perfect for testing file type detection and mismatch identification
- You can recreate these test files by running the PowerShell commands in the project documentation
